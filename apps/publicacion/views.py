from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Mascota, UsuarioRegistrado, Publicacion
from .forms import RegistroFormPublicacion

class PublicaMascota(CreateView):
	model = Publicacion
	template_name = 'AdoptaMascotas/apps/publicacion/publicar.html'
	form_class = RegistroFormPublicacion
	success_url = reverse_lazy('publicacion:publicar')

def listaPublicaciones(request):
	pub = Publicacion.objects.all()
	contexto = {'publicaciones':pub}
	return render(request, 'AdoptaMascotas/apps/publicacion/lista_publicaciones.html', contexto)
	print(request.POST)

def elegirMascotas(request):
	mascotas = Mascota.objects.all()
	return render(request, 'AdoptaMascotas/apps/publicacion/publicar.html', {'mascotas':mascotas})

def mePostulo(request):
	mepostulo = request.get("mepostulo")
	pass
