from django.contrib import admin
from .models import Cliente, Comprobante, Detalle

admin.site.register(Cliente)
admin.site.register(Comprobante)
admin.site.register(Detalle)
