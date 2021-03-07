from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UsuarioRegistrado(AbstractUser):
	direccion = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)

	def __str__(self):
		return(self.first_name + ' ' + self.last_name)

		