from django.conf.urls import url
#from apps.mascota.views import Mascota, Categoria
from .views import RegistroMascota
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='mascota'

urlpatterns = [
    path('registrar/', RegistroMascota.as_view(),  name = 'registrar'),
    path('listar_mascotas/', views.listarMascotas, name='listar_mascotas'),
    path('crearAdopcion/<int:id_mascota>', views.crearAdopcion, name='crearAdopcion'),


  
]

