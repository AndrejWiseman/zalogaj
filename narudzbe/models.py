from django.db import models

class Narudzba(models.Model):
    ime = models.CharField(max_length=100)
    adresa = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    napomena = models.TextField(blank=True, null=True)
    kreirano = models.DateTimeField(auto_now_add=True)
    zavrsena = models.BooleanField(default=False)

    def __str__(self):
        return f"Narudžba #{self.id} - {self.ime}"

class NarudzbaStavka(models.Model):
    narudzba = models.ForeignKey(Narudzba, related_name='stavke', on_delete=models.CASCADE)
    jelo_id = models.IntegerField()  # Ili ForeignKey na Jelo ako želiš
    naziv = models.CharField(max_length=200)
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    kolicina = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.naziv} x {self.kolicina}"
