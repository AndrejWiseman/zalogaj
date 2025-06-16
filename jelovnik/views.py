from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import VrstaJela, Jelo, Dodatak
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
# def index(request):

#     context = {

#     }
#     return render(request, 'index.html', context)


@ensure_csrf_cookie
def jelovnik_view(request):
    vrste = VrstaJela.objects.prefetch_related('jela__dodaci').all()
    return render(request, 'index.html', {'vrste': vrste})




@require_POST
def dodaj_u_korpu(request, jelo_id):
    korpa = request.session.get('korpa', {})
    korpa[str(jelo_id)] = korpa.get(str(jelo_id), 0) + 1
    request.session['korpa'] = korpa
    request.session.modified = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        ukupno_stavki = sum(korpa.values())
        return JsonResponse({'success': True, 'ukupno_stavki': ukupno_stavki})
    else:
        return redirect('index')  # fallback ako POST nije AJAX



def prikazi_korpu(request):
    korpa = request.session.get('korpa', {})
    jela_u_korpi = []

    for jelo_id_str, kolicina in korpa.items():
        jelo_id = int(jelo_id_str)
        jelo = get_object_or_404(Jelo, pk=jelo_id)
        jela_u_korpi.append({
            'jelo': jelo,
            'kolicina': kolicina,
            'ukupno': jelo.cena * kolicina,
        })

    ukupno_svega = sum(item['ukupno'] for item in jela_u_korpi)

    return render(request, 'korpa.html', {
        'stavke': jela_u_korpi,
        'ukupno': ukupno_svega,
    })




@require_POST
def ukloni_iz_korpe(request, jelo_id):
    korpa = request.session.get('korpa', {})

    jelo_id_str = str(jelo_id)
    if jelo_id_str in korpa:
        del korpa[jelo_id_str]
        request.session['korpa'] = korpa
        request.session.modified = True

    return redirect('korpa')