from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.mascota.forms import RegistroForm
from .models import Mascota

class RegistroMascota(CreateView):
	model = Mascota
	template_name = 'AdoptaMascotas/apps/mascota/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:registrar')