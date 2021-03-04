from django.shortcuts import render

# Create your views here.

#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from .models import UsuarioRegistrado

class RegistroUsuario(CreateView):
	model = UsuarioRegistrado
	template_name = 'AdoptaMascotas/apps/usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:registrar')





