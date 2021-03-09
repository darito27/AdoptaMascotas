# Vistas basadas en clases

#from django.views.generic import DetailView

from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView
from django.core.mail import send_mail
from django.conf import settings

def index(request):
	return render (request, 'AdoptaMascotas/templates/index.html')

def prueba(request):
	return render (request, 'AdoptaMascotas/templates/prueba.html')	

def base(request):
	return render (request, 'AdoptaMascotas/templates/base.html')

def politicaPrivacidad(request):
	return render (request, 'AdoptaMascotas/templates/politica_privacidad.html')	

def blog(request):
	return render (request, 'AdoptaMascotas/templates/blog.html')

def sobreNosotros(request):
	return render (request, 'AdoptaMascotas/templates/sobrenosotros.html')


def servicios(request):
	return render (request, 'AdoptaMascotas/templates/servicios.html')
#class Contacto(DetailView):
#	template_name = 'contacto.html'



def contacto (request):
	if request.method == 'POST':
		subject = request.POST['asunto']
		message = 'Soy ' + request.POST['nombre'] + ' ' + request.POST['apellido'] + ' Mi mensaje es el siguiente: ' + request.POST['mensaje'] + ' y este es mi email :' + request.POST['email']
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['mipagina.2021.1@gmail.com']
		send_mail(subject, message, email_from, recipient_list)
		
	return render (request, 'AdoptaMascotas/templates/contacto.html')




