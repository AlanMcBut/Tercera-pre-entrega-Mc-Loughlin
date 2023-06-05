from django import views
from django.urls import  path
from . import views


urlpatterns = [
    path("", views.index, name = "index" ),
    path("crear_placa/", views.anuncio_placa, name= "anuncio placa" )
]