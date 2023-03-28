from django.urls import path
from .views import *

urlpatterns = [
    path('',principal,name='principal'),
    path('iniciosesion/',iniciosesion,name='iniciosesion'),
    path('registro/',registro,name='registro'),
    path('cerrar/',cerrarsesion,name='cerrar')
]
