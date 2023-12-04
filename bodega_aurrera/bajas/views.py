from django.shortcuts import render

# Create your views here.
def view_baja_producto(request):
    return render (request, 'template_base/baja.html', {'page_title': 'BAJAS'})