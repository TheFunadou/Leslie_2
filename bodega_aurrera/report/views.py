from django.shortcuts import render
from django.views.generic import TemplateView
from altas import models
from report.report import report
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, F, Func

import datetime

# Create your views here.

class Index (TemplateView):
    template_name= "report/index.html"


def reporte_ventas_semanales(request):
    
    # # Obtén la fecha de inicio y fin de la semana actual
    # hoy = timezone.now().date()
    # inicio_semana = hoy - timezone.timedelta(days=hoy.weekday())
    # fin_semana = inicio_semana + timezone.timedelta(days=6)
    
    
    list_ventas_s = []
    fecha_hora_actual = datetime.datetime.now()
    # pagos = models.pago.objects.filter(
    #     fecha_hora__gte=timezone.now() - datetime.timedelta(days=7),
    #     fecha_hora__lt=timezone.now(),
    # )
    
    # resultados = pagos.values('folio').annotate(total=Sum('precio'))
     


    # for rs in resultados:
    #     list_ventas_s.append({
    #         'folio': rs['folio'],
    #         'importe':rs['total'],
    #     })
        
    # Obtener la fecha actual y restar 7 días para obtener la fecha de inicio de la semana
    fecha_fin_semana = timezone.now()
    fecha_inicio_semana = fecha_fin_semana - timedelta(days=7)

    # Filtrar registros de la semana actual
    registros_semana_actual = models.pago.objects.filter(fecha_hora__gte=fecha_inicio_semana, fecha_hora__lte=fecha_fin_semana)

    # Realizar la suma por folio
    suma_por_folio = registros_semana_actual.values('folio').annotate(total_precio=Sum('precio'))
    
    
    # Filtrar registros de la semana actual
    registros_semana_actual = models.pago.objects.filter(fecha_hora__gte=fecha_inicio_semana, fecha_hora__lte=fecha_fin_semana)

    # Calcular la suma total de la columna precio
    suma_total_precio = registros_semana_actual.aggregate(total_precio=Sum('precio'))
    
    cast_suma_total = str(suma_total_precio['total_precio'])

    # Imprimir los resultados
    for suma in suma_por_folio:
        list_ventas_s.append({
            'folio': suma['folio'],
            'importe':suma['total_precio'],
        })
        
    data = {
        'list_venta_s': list_ventas_s,
        'fecha_hora':fecha_hora_actual.strftime("%d/%m/%Y %H:%M"),
        'total':f'{cast_suma_total} M.N',
    }
        
    return report(request, 'ventas_semanales', data)

def reporte_ventas_mensuales(request):
    
    # # Obtén la fecha de inicio y fin de la semana actual
    # hoy = timezone.now().date()
    # inicio_semana = hoy - timezone.timedelta(days=hoy.weekday())
    # fin_semana = inicio_semana + timezone.timedelta(days=6)
    
    
    list_ventas_s = []
    fecha_hora_actual = datetime.datetime.now()
    # pagos = models.pago.objects.filter(
    #     fecha_hora__gte=timezone.now() - datetime.timedelta(days=7),
    #     fecha_hora__lt=timezone.now(),
    # )
    
    # resultados = pagos.values('folio').annotate(total=Sum('precio'))
     


    # for rs in resultados:
    #     list_ventas_s.append({
    #         'folio': rs['folio'],
    #         'importe':rs['total'],
    #     })
        
    # Obtener la fecha actual y restar 7 días para obtener la fecha de inicio de la semana
    fecha_fin_semana = timezone.now()
    fecha_inicio_semana = fecha_fin_semana - timedelta(days=7)

    # Filtrar registros de la semana actual
    registros_semana_actual = models.pago.objects.filter(fecha_hora__gte=fecha_inicio_semana, fecha_hora__lte=fecha_fin_semana)

    # Realizar la suma por folio
    suma_por_folio = registros_semana_actual.values('folio').annotate(total_precio=Sum('precio'))
    
    
    # Filtrar registros de la semana actual
    registros_semana_actual = models.pago.objects.filter(fecha_hora__gte=fecha_inicio_semana, fecha_hora__lte=fecha_fin_semana)

    # Calcular la suma total de la columna precio
    suma_total_precio = registros_semana_actual.aggregate(total_precio=Sum('precio'))
    
    cast_suma_total = str(suma_total_precio['total_precio'])

    # Imprimir los resultados
    for suma in suma_por_folio:
        list_ventas_s.append({
            'folio': suma['folio'],
            'importe':suma['total_precio'],
        })
        
    data = {
        'list_venta_s': list_ventas_s,
        'fecha_hora':fecha_hora_actual.strftime("%d/%m/%Y %H:%M"),
        'total':f'{cast_suma_total} M.N',
    }
        
    return report(request, 'ventas_mensuales', data)
    
    
    
    