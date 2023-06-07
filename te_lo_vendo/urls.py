"""
URL configuration for te_lo_vendo project.

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
from bienvenidos.views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido),
]

'''Identifique los diferentes archivos creados por Django al crear 
un proyecto y una aplicación. Describa en palabras simples la 
utilidad de cada script. '''


# manage.py: es el scripts de gestión de los comandos para el proyecto django.

# settings.py: acá se configura el proyecto. 

# urls.py: se mapean las diferentes aplicaciones y vistas.

# views.py: se definen las vistas de la aplicación, controla la lógica. 

# admin.py: el panel de administrador de django. 