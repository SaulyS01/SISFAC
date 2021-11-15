from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente

class clienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Create your views here.
