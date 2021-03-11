from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.mascota.forms import RegistroForm
from .models import Mascota, Categoria, Sexo, Postulantes, UsuarioRegistrado 
from django.http import HttpResponse

class RegistroMascota(CreateView):
	model = Mascota
	template_name = 'AdoptaMascotas/apps/mascota/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:registrar')

def listarMascotas(request):
	mascotas = Mascota.objects.all()
	return render(request, 'AdoptaMascotas/apps/mascota/listar_mascotas.html',
	 {'mascotas':mascotas})


def postularAdopcion(request, id_mascota):
	mascota = id_mascota
	postulante = request.user.id
	p = Postulantes(id_mascota_id=mascota, usuario=postulante, id_usuario_id=postulante)
	p.save()
	return redirect('mascota:listar_mascotas')


def listarPostulantes(request):
	postulantes = Postulantes.objects.all()
	print (postulantes)
	return render(request, 'AdoptaMascotas/apps/mascota/listar_postulantes.html',
	 {'postulantes':postulantes})