from django.conf.urls import url

from .views import PublicaMascota
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='publicacion'

urlpatterns = [
    url(r'^publicar/', PublicaMascota.as_view(),  name = 'publicar'),
    #path('publicar/', views.elegirMascotas),
    path('lista_publicaciones/', views.listaPublicaciones),

  
]
