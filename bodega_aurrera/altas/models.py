from django.db import models

# Create your models here.


class alta_de_productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, null=False)
    proveedor = models.CharField(max_length=50)
    existencias = models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    # imagen_producto = models.ImageField(upload_to=)
    

class pago(models.Model):
    serial =  models.BigAutoField(primary_key=True)
    folio = models.BigIntegerField()
    producto = models.ForeignKey(alta_de_productos,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    
    class Meta:
        unique_together = ('serial','folio', 'producto')
        
        



