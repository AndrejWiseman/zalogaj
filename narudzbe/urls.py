from django.urls import path
from .views import kreiraj_narudzbu, korpa_view

urlpatterns = [
    path('naruci/', kreiraj_narudzbu, name='kreiraj_narudzbu'),
    path('korpa/', korpa_view, name='korpa'),
]
