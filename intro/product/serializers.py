from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    in_stock = serializers.BooleanField()


class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    in_stock = serializers.BooleanField()

    def create(self, validated_data):
        print('SERIALIZER', validated_data)
        return Product.objects.create(**validated_data)
        # INSERT INTO table ...
