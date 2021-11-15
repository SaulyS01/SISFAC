from rest_framework import fields, serializers
from .models import Cliente

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cliente
        fields=['id', 'dni', 'nombre', 'ruc', 'razon', 'dire']
        