from django.conf.urls import url
from apps.usuario.views import RegistroUsuario
from . import views
from django.contrib.auth import login
from django.contrib.auth import logout as do_logout
from django.urls import path

app_name='usuario'

urlpatterns = [
    url(r'^registrar/', RegistroUsuario.as_view(),  name = 'registrar'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
#    url(r'^login/', login.as_view('template_name'=='login.html') ,  name = 'login'),
   
]

