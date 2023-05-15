from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_products(request: Request):
    queryset = Product.objects.all()
    # SELECT * FROM product;
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


# TODO: разверните 3 проекта и залейте на 3 разных репозитория на гитхаб