from django.db import models

# Create your models here.

from django.db import models
from django.utils.timezone import now
from apps.usuario.models import UsuarioRegistrado
from apps.mascota.models import Mascota

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField( verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(default=now, verbose_name="Fecha de publicación")
    imagen = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    autor = models.ForeignKey(UsuarioRegistrado, on_delete=models.CASCADE, verbose_name="Autor")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.titulo