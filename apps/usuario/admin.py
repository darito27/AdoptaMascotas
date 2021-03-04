from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import UsuarioRegistrado

admin.site.register(UsuarioRegistrado, UserAdmin)

