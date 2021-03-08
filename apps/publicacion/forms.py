from django.forms import ModelForm
from .models import Publicacion


class RegistroFormPublicacion(ModelForm):

	class Meta:
		model = Publicacion
		fields = [
			'titulo',
			'imagen',
			'contenido',
			'autor'
						
		]

		labels = {
			'titulo': 'Titulo',
			'imagen' : 'Imagen',
			'contenido' : 'Contenido',
			'autor' : 'Autor',
			
		}
