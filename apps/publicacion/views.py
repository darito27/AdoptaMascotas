from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Mascota, UsuarioRegistrado, Post
from .forms import RegistroFormPost

class PublicaMascota(CreateView):
	model = Post
	template_name = 'AdoptaMascotas/apps/publicacion/publicar.html'
	form_class = RegistroFormPost
	success_url = reverse_lazy('publicacion:publicar')