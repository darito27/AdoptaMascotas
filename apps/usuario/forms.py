#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioRegistrado

class RegistroForm(UserCreationForm):


	class Meta:
		model = UsuarioRegistrado
		fields = [
			'username',
			'first_name',
			'last_name',
			'direccion',
			'ciudad',
			'telefono',
			'email',
			
		]

		labels = {
			'username':'Usuario',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'direccion' : 'Direccion',
			'ciudad' : 'Ciudad',
			'telefono' : 'Telefono',
			'email':'eMail',

		}


