from django.contrib import admin

# Register your models here.

from .models import Categoria, Sexo, Mascota

admin.site.register(Categoria)
admin.site.register(Sexo)
admin.site.register(Mascota)


class ServicioAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')