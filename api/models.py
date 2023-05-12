from django.db import models

# Create your models here.


class articulo(models.Model):
    id = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio_sin_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto_aplicable = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class pedido(models.Model):
    id = models.AutoField(primary_key=True)
    lista_articulos = models.JSONField()
    precio_total_sin_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total_con_impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion_pedido = models.DateTimeField(auto_now_add=True)