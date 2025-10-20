from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from store.apps.products.models import Product
from store.apps.products.serializers import ProductSerializer


class ProductList(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    @swagger_auto_schema(
        tags=['Products'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Filter products by title',
                ),
            },
            required=[]
        ),
        responses={200: ProductSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        qs = self.get_queryset()
        data = request.data
        title = data.get('title')
        if title:
            qs.filter(title__icontains=title)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
