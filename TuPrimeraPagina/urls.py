"""
URL configuration for TuPrimeraPagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from blog.views import inicio, crear_autor, crear_categoria
from blog.views import crear_post
from blog.views import inicio, crear_autor, crear_categoria, crear_post, buscar_post


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria/nueva/', crear_categoria, name='crear_categoria'),
    path('autor/nuevo/', crear_autor, name='crear_autor'),
    path('admin/', admin.site.urls),
    path('post/nuevo/', crear_post, name='crear_post'),
    path('buscar/', buscar_post, name='buscar_post'),
]
