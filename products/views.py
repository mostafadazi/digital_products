
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product, File
from.serializers import CategorySerializer, ProductSerializer, FileSerializer
from rest_framework import status


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True, context={'request' : request})

        return Response(serializer.data)
    

class ProductListDetailView(APIView):
    def get(self, request, pk):

        try:
            product = Product.objects.get(pk = pk)
        
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, context = {'request': request})

        return Response(serializer.data)