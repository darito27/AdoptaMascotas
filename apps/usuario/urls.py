from django.conf.urls import url
from apps.usuario.views import RegistroUsuario
from . import views
from django.contrib.auth import login
from django.contrib.auth import logout as do_logout
from django.urls import path

app_name='usuario'

urlpatterns = [
    url(r'^registrar/', RegistroUsuario.as_view(),  name = 'registrar'),
    url(r'^login/', views.login, name = 'login'),
    url(r'^logout/', views.logout, name = 'logout'),
    url(r'^lista_publicaciones/', views.listaUsuarios, name = 'logout'),
   
]

