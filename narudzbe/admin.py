from django.contrib import admin
from .models import Narudzba, NarudzbaStavka

class NarudzbaStavkaInline(admin.TabularInline):
    model = NarudzbaStavka
    extra = 0

@admin.register(Narudzba)
class NarudzbaAdmin(admin.ModelAdmin):
    list_display = ('ime', 'id', 'adresa', 'telefon', 'zavrsena')  # prilagodi polja po potrebi
    inlines = [NarudzbaStavkaInline]

@admin.register(NarudzbaStavka)
class NarudzbaStavkaAdmin(admin.ModelAdmin):
    list_display = ('narudzba', 'naziv', 'kolicina', 'cena')
