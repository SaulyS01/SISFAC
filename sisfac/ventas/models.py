from django.db import models
from django.db.models.fields.related import ForeignKey

class Cliente(models.Model):

    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=10)
    razon = models.CharField(max_length=50)
    dire = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.dni

class Comprobante(models.Model):

    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    comp = models.CharField(max_length=20, )
    numfac = models.CharField(max_length=10)
    numboleta = models.CharField(max_length=10)
    fecha = models.DateTimeField()
    igv = models.FloatField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Comprobante")
        verbose_name_plural = ("Comprobantes")

    def __str__(self):
        return self.cliente

class Detalle(models.Model):

    comp = models.ForeignKey("Comprobante", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    producto = models.ForeignKey("kardex.Producto", on_delete=models.CASCADE)
    importe = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Detalle")
        verbose_name_plural = ("Detalles")

    def __str__(self):
        return self.cantidad
