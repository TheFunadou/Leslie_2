from django.urls import path
from report.report import *
from report import views

app_name='report'

urlpatterns = [
    path('edit/<str:report_type>/', edit , name='report_edit'),
    path('run/', run , name='report_run'),
    path('save/<str:report_type>/', save , name='report_save'),
    
    path('ventas_semanales/', views.reporte_ventas_semanales, name='reporte_ventas_s'),
]