from django.forms import ModelForm
from .models import Post


class RegistroFormPost(ModelForm):

	class Meta:
		model = Post
		fields = [
			'titulo',
			'contenido',
			'autor'
						
		]

		labels = {
			'titulo': 'Titulo',
			'contenido' : 'Contenido',
			'autor' : 'Autor',
			
		}
