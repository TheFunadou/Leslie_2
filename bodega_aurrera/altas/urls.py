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
from django.urls import path
from altas import views as views

app_name='altas'

urlpatterns = [
    path('venta_productos/', views.view_venta , name='venta'),
    path('alta_articulo/',views.view_alta_articulo, name='alta_articulo'),
    path('registrar_articulo/',views.registrar_articulo, name='registrar_articulo'),
    path('agregar_al_carrito/',views.agregar_carrito, name='agregar_al_carrito'),
    path('pagar/',views.pagar, name='pagar'),
    path('ticket_pago/<str:folio>/<str:cajero>/<str:subtotal>/<str:iva>/<str:total>/<str:descuento>/',views.ticket_compra, name='report_ticket_compra'),
    path('reporte_productos/',views.report_productos, name='report_productos')
]
