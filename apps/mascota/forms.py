#from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Mascota, Categoria, Sexo


class RegistroForm(ModelForm):

	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'tipo',
			'raza',
			'sexo',
			'contenido',
			'edad_aproximada',
			
		]

		labels = {
			'nombre': 'Nombre',
			'tipo' : 'Tipo',
			'raza' : 'Raza',
			'sexo' : 'Sexo',
			'contenido' : 'Contenido',
			'edad_aproximada': 'Edad Aproximada',

		}


