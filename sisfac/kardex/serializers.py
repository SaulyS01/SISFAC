from rest_framework import fields, serializers
from .models import Proveedor

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Proveedor
        fields=['id', 'razonSocial', 'ruc', 'dire', 'ciudad', 'celular1',
        'celular2', 'telef1', 'telef2', 'contacto', 'email', 'web', 'banco',
        'cuenta']
        