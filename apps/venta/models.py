from django.db import models

from apps.cotizacion.models import Cotizacion

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    n_orden_compra = models.IntegerField()
    fecha_orden_compra = models.DateField()
    moneda = models.IntegerField()
    tipo_cambio = models.CharField(max_length=50)
    fecha_entrega_oc = models.DateField()
    fecha_facturacion = models.DateField()
    utilidad_esperada = models.IntegerField()
    observaciones = models.CharField(max_length=100)

    class Meta:
        db_table = 'venta'