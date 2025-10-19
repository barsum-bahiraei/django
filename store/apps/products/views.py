from django.shortcuts import render
from rest_framework import generics

from store.apps.products.models import Product
from store.apps.products.serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
