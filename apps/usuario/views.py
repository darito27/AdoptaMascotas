from django.shortcuts import render, redirect

# Create your views here.

#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from .models import UsuarioRegistrado
# AGREGADO PARA LOGIN
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

class RegistroUsuario(CreateView):
	model = UsuarioRegistrado
	template_name = 'AdoptaMascotas/apps/usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:registrar')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('http://127.0.0.1:8000/index/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "AdoptaMascotas/apps/usuario/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('http://127.0.0.1:8000/index/')