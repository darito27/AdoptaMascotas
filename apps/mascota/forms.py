#from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Mascota


class RegistroForm(ModelForm):

	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'tipo',
			'raza',
			'sexo',
			'edad_aproximada',
		]

		labels = {
			'nombre': 'Nombre',
			'tipo' : 'Tipo',
			'raza' : 'Raza',
			'sexo' : 'Sexo',
			'edad_aproximada': 'Edad Aproximada',
		}


