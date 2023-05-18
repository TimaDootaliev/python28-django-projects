from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer


@api_view(['GET'])
def get_products(request: Request):
    queryset = Product.objects.all()
    # SELECT * FROM product;
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request: Request):
    data = request.data
    print('VIEW', data)
    serializer = ProductCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': 'Created successfully'})


@api_view(['GET'])
def get_one_product(reqeust: Request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'message': f'Product with {id} not found'}, status=404)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)
    # SELECT * FROM product WHERE id = id;


@api_view(['DELETE'])
def delete_product(request: Request, id):
    query = Product.objects.filter(id=id)
    product = get_object_or_404(query)
    title = product.title
    product.delete()
    return Response({'message': f'Product with {title} id successfully deleted'}, status=204)


@api_view(['PUT'])
def update_product(request: Request, id):
    query = Product.objects.get(id=id)
    product = get_object_or_404(query)
    serializer = ProductSerializer(query, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# TODO: update product

# TODO: разверните 3 проекта и залейте на 3 разных репозитория на гитхаб
