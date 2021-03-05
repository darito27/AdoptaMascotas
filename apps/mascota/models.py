from django.db import models
from apps.usuario.models import UsuarioRegistrado


# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=20)
	tipo = models.CharField(max_length=20)
	raza = models.CharField(max_length=20)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_adopcion = models.DateField(null = True, blank = True)
	duenio =  models.ForeignKey(UsuarioRegistrado, null = True, blank = True, on_delete = models.CASCADE)
	