"""AdoptaMascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from AdoptaMascotas.views import index, prueba


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name = 'Inicio'),
    path('base/', views.base, name = 'Base'),
    path('prueba/', views.prueba, name = 'Prueba'),
    path('contacto/', views.contacto, name = 'Contacto'),
    path('blog/', views.blog, name = 'Blog'),
    path('sobrenosotros/', views.sobreNosotros, name = 'Sobre Nosotros'),
    path('servicios/', views.servicios, name = 'Servicios'),

]
