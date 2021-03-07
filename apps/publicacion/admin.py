from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)

class PostsAdmin(admin.ModelAdmin):
	readonly_fields=('created', 'updated')