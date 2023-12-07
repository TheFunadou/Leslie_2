from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from altas import models
from altas.models import alta_de_productos
from django.db.models import Sum, Max
from report.report import report
import datetime
from django.core.files.storage import default_storage
from django.conf import settings
import os


# Create your views here.
def view_venta(request):
    return render (request, 'templates_altas/carrito_compras.html', {'page_title': 'VENTA'})

def view_alta_articulo(request):
    return render (request, 'templates_altas/alta_articulo.html', {'page_title': 'REGISTRAR NUEVO PRODUCTO'})

# DAR DE ALTA PRODUCTOS EN LA BASE DE DATOS
def registrar_articulo(request):
    
    if request.method == 'POST':
        # Crea el objeto de modelo con los datos del formulario y la ruta de la imagen
        imagen_producto = request.FILES.get('img_prod', None)
        
        producto = alta_de_productos.objects.create(
            nombre=request.POST['nom_producto'],
            marca=request.POST['marca'],
            modelo=request.POST['modelo'],
            proveedor=request.POST['proveedor'],
            existencias=request.POST['existencias'],
            precio=request.POST['precio']
        )
        
        if imagen_producto:
            # Guardar la imagen en la ubicación especificada
            producto.imagen_producto.save(imagen_producto.name, imagen_producto)

        producto.save()
    
        return redirect('main')
    
def agregar_carrito(request):
    if request.method == 'GET':
        id_producto = request.GET.get('id_producto')
        
    index_prod = models.alta_de_productos.objects.get(id_producto=id_producto)
    
    return JsonResponse({'id_producto':index_prod.id_producto, 'nombre':index_prod.nombre, 'marca':index_prod.marca, 'precio':index_prod.precio})


def pagar(request):
    if request.method == 'GET':
        lista_id_productos = request.GET.getlist('lista_id_productos[]')
        lista_cantidad = request.GET.getlist('lista_cantidad[]')
        subtotal = request.GET.get('subtotal')
        iva = request.GET.get('iva')
        total = request.GET.get('total')
        cajero = request.GET.get('cajero')
    
    cajero = 'N_A' if cajero == '' else cajero
    
    # Obtener el último folio
    max_folio = models.pago.objects.aggregate(max_folio=Max('folio'))['max_folio']
    nvo_folio = max_folio + 1 if max_folio is not None else 1


    if len(lista_id_productos) == len(lista_cantidad):
            for id_producto, cantidad in zip(lista_id_productos, lista_cantidad):
                producto = models.alta_de_productos.objects.get(id_producto=id_producto)
                precio = float(producto.precio) * float(cantidad)
                # print(precio)
                pago = models.pago.objects.create(
                    folio = nvo_folio, producto=producto, cantidad=cantidad, precio = precio
                )
                producto.existencias = int(producto.existencias) - int(cantidad)
                producto.save()
    
    return JsonResponse({'folio':pago.folio, 'cajero':cajero, 'subtotal':subtotal, 'iva':iva, 'total':total})
    

def ticket_compra(request,folio,cajero,subtotal,iva,total):
    query_pago = models.pago.objects.select_related('producto').all().filter(folio=folio)
    fecha_hora_actual = datetime.datetime.now()
    list_ticket = []
    
    for rs in query_pago:
        list_ticket.append({
            'id_producto': str(rs.producto.id_producto),
            'nombre_producto':rs.producto.nombre,
            'precio_producto':str(rs.producto.precio),
            'cantidad_producto':str(rs.cantidad),
            'total_producto': str(rs.precio)
        })
        
    data = {
        'list_ticket': list_ticket,
        'fecha_hora':fecha_hora_actual.strftime("%d/%m/%Y %H:%M"),
        'cajero':cajero,
        'subtotal':f'{subtotal} M.N',
        'iva':f'{iva} M.N',
        'total':f'{total} M.N'
    }
    
    for rs_2 in query_pago:
        data['folio_pago']=str(rs_2.folio)

        
    return report(request, 'ticket_compra', data)
        
def report_productos(request):
    lista_productos = []
    fecha_hora_actual = datetime.datetime.now()
    query_productos = models.alta_de_productos.objects.all()
    
    for rs in query_productos:
        lista_productos.append({
            'id': rs.id_producto,
            'nombre':rs.nombre,
            'marca':rs.marca,
            'modelo':rs.modelo,
            'proveedor':rs.proveedor,
            'existencias':rs.existencias,
            'precio':rs.precio
        })
        
    data = {
        'list_productos':lista_productos,
        'fecha_hora':fecha_hora_actual.strftime("%d/%m/%Y %H:%M"),
    }
    
    return report(request,'report_productos',data)