from django.shortcuts import render, redirect
from .models import Narudzba, NarudzbaStavka
from .forms import NarudzbaForm
from jelovnik.models import Jelo  # ili kako već importuješ model Jelo

def kreiraj_narudzbu(request):
    korpa = request.session.get('korpa', {})
    if not korpa:
        return redirect('index')

    if request.method == 'POST':
        form = NarudzbaForm(request.POST)
        if form.is_valid():
            narudzba = form.save()

            for jelo_id, kolicina in korpa.items():
                jelo = Jelo.objects.get(id=jelo_id)
                NarudzbaStavka.objects.create(
                    narudzba=narudzba,
                    jelo_id=jelo.id,
                    naziv=jelo.naziv,
                    cena=jelo.cena,
                    kolicina=kolicina
                )
            request.session['korpa'] = {}
            request.session.modified = True
            return redirect('index')
    else:
        form = NarudzbaForm()

    return render(request, 'kreiraj_narudzbu.html', {'form': form})

def korpa_view(request):
    korpa = request.session.get('korpa', {})
    stavke = []

    for jelo_id, kolicina in korpa.items():
        try:
            jelo = Jelo.objects.get(id=jelo_id)
            stavke.append({
                'jelo': jelo,
                'kolicina': kolicina,
                'ukupno': jelo.cena * kolicina,
            })
        except Jelo.DoesNotExist:
            pass

    ukupno = sum(item['ukupno'] for item in stavke)
    return render(request, 'narudzbe/korpa.html', {'stavke': stavke, 'ukupno': ukupno})
