# Vistas basadas en clases

#from django.views.generic import DetailView

from django.shortcuts import render, HttpResponse

def index(request):
	return render (request, 'AdoptaMascotas/templates/index.html')

def prueba(request):
	return render (request, 'AdoptaMascotas/templates/prueba.html')	