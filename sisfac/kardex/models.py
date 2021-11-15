from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Marca(models.Model):

    desc = models.CharField(max_length=70)
    logo = models.ImageField(upload_to="Marca", null=True, blank=True)

    class Meta:
        verbose_name = ("Marca")
        verbose_name_plural = ("Marcas")

    def __str__(self):
        return self.desc

class Grupo(models.Model):

    desc = models.CharField(max_length=30)
    grupo_id = models.ForeignKey("Grupo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Grupo")
        verbose_name_plural = ("Grupos")

    def __str__(self):
        return self.desc

TIPO_MEDIDA = [
    ('BJ', 'BALDE'),
    ('BG', 'BOLSA'),
    ('BX', 'CAJA'),
    ('KG', 'KILOGRAMO'),
    ('LTR', 'LITRO'),
    ('NIU', 'UNIDAD'),
]

class Producto(models.Model):

    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    media = models.CharField(max_length=20, choices=TIPO_MEDIDA)
    grupo = models.ForeignKey("Grupo", on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=15)
    desc = models.CharField(max_length=30)
    image = models.ImageField(upload_to="producto", null=True, blank=True)
    maximo = models.IntegerField()
    minimo = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.marca

class Proveedor(models.Model):

    razonSocial = models.CharField(max_length=30)
    ruc = models.CharField(max_length=15)
    dire = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=20)
    celular1 = models.CharField(max_length=15)
    celular2 = models.CharField(max_length=15)
    telef1 = models.CharField(max_length=15)
    telef2 = models.CharField(max_length=15)
    contacto = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    web = models.CharField(max_length=30)
    banco = models.CharField(max_length=30)
    cuenta = models.CharField(max_length=40)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedors")

    def __str__(self):
        return self.razonSocial

TIPO_OPER = [
    ('VENTA', 'VENTA NACIONAL'),
    ('COMPRA', 'COMPRA NACIONAL'),
    ('DEVO', 'DEVOLUCIÓN RECIBIDA'),
    ('OTROS', 'OTROS'),
]

TIPO_COMP = [
    ('Factura', 'Factura'),
    ('Boleto', 'Boleto de Venta'),
    ('Guia', 'Guía de remisión'),
]

class Kardex(models.Model):

    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    oper = models.CharField(max_length=50, choices=TIPO_OPER)
    comp = models.CharField(max_length=20, choices=TIPO_COMP)
    proveedor = models.ForeignKey("Proveedor", on_delete=CASCADE)
    fecha = models.DateTimeField()
    serie = models.CharField(max_length=8)
    numero = models.CharField(max_length=10)
    cant = models.IntegerField()
    cost = models.FloatField()
    costTotal = models.FloatField()
    scant = models.IntegerField()
    scost = models.FloatField()
    scostTotal = models.FloatField()
    xcant = models.IntegerField()
    xcost = models.FloatField()
    xcostTotal = models.FloatField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Kardex")
        verbose_name_plural = ("Kardexs")

    def __str__(self):
        return self.producto
