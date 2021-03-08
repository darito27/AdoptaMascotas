from django.contrib import admin

# Register your models here.

from .models import Publicacion

admin.site.register(Publicacion)

class PostsAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')