from django.db import models


class VrstaJela(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    redosled = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['redosled']


    def __str__(self):
        return self.naziv


class Jelo(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    vrsta = models.ForeignKey(VrstaJela, on_delete=models.CASCADE, related_name='jela')
    posno = models.BooleanField(default=False)
    preporuceno = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv


class Dodatak(models.Model):
    naziv = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    jela = models.ManyToManyField(Jelo, related_name='dodaci', blank=True)

    def __str__(self):
        return self.naziv
