from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from altas import models

# Create your views here.
def view_baja_producto(request):
    return render (request, 'templates_bajas/baja.html', {'page_title': 'BAJAS'})

def buscar_articulo(request):
    if request.method=='GET':
        id_producto = request.GET.get('id_producto')
        
    query_producto = models.alta_de_productos.objects.all().filter(id_producto = id_producto)
    
    if query_producto.exists():
        # Serializar
        list_producto = [{'nombre':rs.nombre, 'marca':rs.marca, 'modelo':rs.modelo, 'proveedor':rs.proveedor, 'existencias':rs.existencias, 'precio':rs.precio} for rs in query_producto]
        
        return JsonResponse({'info_producto':list_producto, 'mensaje': ''})
    else:
        return JsonResponse({'mensaje':'producto no encontrado'})

def borrar_articulo(request):
    if request.method=='GET':
        id_producto = request.GET.get('id_producto')
        
    query_producto = models.alta_de_productos.objects.get(id_producto=id_producto)
    
    query_producto.delete()
    
    return JsonResponse({'mensaje':'producto eliminado'})