
from django.contrib import admin
from .models import Marca, Grupo, Producto, Proveedor, Kardex

admin.site.register(Marca)
admin.site.register(Grupo)
admin.site.register(Proveedor)
admin.site.register(Kardex)
