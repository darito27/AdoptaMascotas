from django.conf.urls import url
from apps.mascota.views import Mascota
from .views import RegistroMascota
from django.urls import path

app_name='mascota'

urlpatterns = [
    path('registrar/', RegistroMascota.as_view(),  name = 'registrar'),

  
]

