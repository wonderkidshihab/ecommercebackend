from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
# Its handling two different requests, one for the list of products (GET) and creating a new product (POST).
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer