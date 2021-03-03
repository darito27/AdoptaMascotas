# Vistas basadas en clases

#from django.views.generic import DetailView

from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView

def index(request):
	return render (request, 'AdoptaMascotas/templates/index.html')

def prueba(request):
	return render (request, 'AdoptaMascotas/templates/prueba.html')	

def base(request):
	return render (request, 'AdoptaMascotas/templates/base.html')


def contacto(request):
	return render (request, 'AdoptaMascotas/templates/contacto.html')

def blog(request):
	return render (request, 'AdoptaMascotas/templates/blog.html')

def sobreNosotros(request):
	return render (request, 'AdoptaMascotas/templates/sobrenosotros.html')


def servicios(request):
	return render (request, 'AdoptaMascotas/templates/servicios.html')
#class Contacto(DetailView):
#	template_name = 'contacto.html'