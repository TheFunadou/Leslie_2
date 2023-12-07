from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from altas import models

# Create your views here.
def view_modificaciones(request):
    return render (request, 'templates_mod/modificacion_articulo.html', {'page_title': 'MODIFICACIONES ARTICULO'})

def modificar_articulo(request):
    if request.method=='GET':
        id_producto = request.GET.get('id_producto')
        print(id_producto)
        nombre = request.GET.get('nombre')
        marca = request.GET.get('marca')
        modelo = request.GET.get('modelo')
        proveedor = request.GET.get('proveedor')
        existencias = request.GET.get('existencias')
        precio = request.GET.get('precio')
        
    query_articulo = models.alta_de_productos.objects.get(id_producto = id_producto)
    
    query_articulo.nombre = nombre
    query_articulo.marca = marca
    query_articulo.modelo = modelo
    query_articulo.proveedor = proveedor
    query_articulo.existencias = existencias
    query_articulo.precio = precio
    query_articulo.save()
        
    return JsonResponse({'mensaje':'producto modificado exitosamente'})