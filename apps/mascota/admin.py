from django.contrib import admin

# Register your models here.

from .models import Mascota, Categoria, Sexo

admin.site.register(Mascota)
admin.site.register(Categoria)
admin.site.register(Sexo)


class ServicioAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')
