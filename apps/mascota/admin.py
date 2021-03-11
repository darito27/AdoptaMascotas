from django.contrib import admin

# Register your models here.

from .models import Categoria, Sexo, Mascota, Postulantes

admin.site.register(Categoria)
admin.site.register(Sexo)
admin.site.register(Mascota)
admin.site.register(Postulantes)


class ServicioAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')