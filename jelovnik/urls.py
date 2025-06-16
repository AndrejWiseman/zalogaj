from django.urls import path
from .views import  jelovnik_view, dodaj_u_korpu, prikazi_korpu, ukloni_iz_korpe


urlpatterns = [
    # path('', index, name='index'),
    path('', jelovnik_view, name='index'),

    path('dodaj/<int:jelo_id>/', dodaj_u_korpu, name='dodaj_u_korpu'),
    path('korpa/', prikazi_korpu, name='korpa'),
    path('ukloni/<int:jelo_id>/', ukloni_iz_korpe, name='ukloni_iz_korpe'),

]
