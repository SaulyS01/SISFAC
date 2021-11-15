from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProveedorSerializer
from .models import Proveedor

class proveedorViewSet (viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
