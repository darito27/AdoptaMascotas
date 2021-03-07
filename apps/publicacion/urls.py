from django.conf.urls import url

from .views import PublicaMascota
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name='publicacion'

urlpatterns = [
    url(r'^publicar/', PublicaMascota.as_view(),  name = 'publicar'),

  
]
