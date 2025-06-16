from django import forms
from .models import Narudzba

class NarudzbaForm(forms.ModelForm):
    class Meta:
        model = Narudzba
        fields = ['ime', 'adresa', 'telefon', 'napomena']
