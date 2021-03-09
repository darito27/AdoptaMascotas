from django.db import models
from apps.usuario.models import UsuarioRegistrado

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, help_text="Ingrese el tipo de mascota: Perro, Gato, Reptil, Ave, Otro")
    def __str__(self):
    	return self.categoria

class Sexo(models.Model):
	sex = models.CharField(max_length=50, help_text="Ingrese el sexo de la mascota: Macho o Hembra u Otro")
	def __str__(self):
		return self.sex

class Mascota(models.Model):
	nombre = models.CharField(max_length=20)
	tipo =  models.ForeignKey(Categoria, null = True, blank = True, on_delete = models.CASCADE)
	sexo = models.ForeignKey(Sexo, on_delete = models.CASCADE)
	raza = models.CharField(max_length=20)
	edad_aproximada = models.IntegerField()
	imagen = models.ImageField(null = True, blank = True, upload_to='mascotas')
	contenido = models.TextField( verbose_name="Contenido", null = True, blank = True)
	fecha_adopcion = models.DateField(null = True, blank = True)
	duenio =  models.ForeignKey(UsuarioRegistrado, null = True, blank = True, on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return(" %s es un %s  %s de raza %s " %(self.nombre, self.tipo, self.sexo, self.raza))


