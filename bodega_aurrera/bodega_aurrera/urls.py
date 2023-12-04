"""
URL configuration for bodega_aurrera project.

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
from django.urls import path,include
from bodega_aurrera import views_project
#reporrbro
from report.views import Index
from report.report import *
#RUTAS GLOBALES


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_project.main , name='main'),
    path('make_report/', Index.as_view(), name='index'),
    
    #IMPORTAR APLICACIONES
    path('altas/',include('altas.urls', namespace='altas')),
    path('bajas/',include('bajas.urls', namespace='bajas')),
    path('modificaciones/',include('modificaciones.urls',namespace='modificaciones')),
    path('report/', include(('report.urls', 'report'))),
    
    #IMPORTAR FUNCIONALIDADES DE REPORTES
    path('edit/<str:report_type>/', edit , name='report_edit'),
    path('run/', run , name='report_run'),
    path('save/<str:report_type>/', save , name='report_save'),
]
