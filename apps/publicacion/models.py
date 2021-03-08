from django.db import models

# Create your models here.

from django.db import models
from django.utils.timezone import now
from apps.usuario.models import UsuarioRegistrado
from apps.mascota.models import Mascota

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField( verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True, verbose_name="Imagen")
    autor = models.ForeignKey(UsuarioRegistrado, on_delete=models.CASCADE, verbose_name="Autor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "publicacion"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return("El titulo es:%s" %(self.titulo))

