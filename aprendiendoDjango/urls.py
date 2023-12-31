"""
URL configuration for aprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#Import my views
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('hola_mundo/', views.hola_mundo, name = "HolaMundo"),
    path('hola_mundo/<int:redirigir>', views.hola_mundo, name = "HolaMundo"),
    path('biblioteca/', views.biblioteca, name = "biblioteca"),
    path('contacto/>', views.contacto, name = "contacto"),
    path('contacto/<str:nombre>', views.contacto, name = "contacto"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name = "contacto"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name = "CrearArticulo"),
    path('articulo/', views.articulo, name = "articulo"),
    path('editar_articulo/<int:id>', views.editar_articulo,name = "EditarArticulo"),
    path('articulos/', views.articulos, name = 'articulos'),
    path('borrar_articulo/<int:id>', views.borrar_articulo, name = 'borrar'),
    path('crear_articulo/', views.create_article, name = "crear"),
    path('save_articulo/' , views.save_articulo, name = "save")
]
