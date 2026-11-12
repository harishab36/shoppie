from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.db.models import ObjectDoesNotExist

# Create your views here.

@api_view(['GET'])
def getRequest(request):
    return Response('Hello world !!!')

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):

    product = Product.objects.filter(_id = pk).first()

    print(product)
    serializer = ProductSerializer(product, many = False)
    return Response(serializer.data if product != None else "Product not found")