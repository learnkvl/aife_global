from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # To return full category object

    class Meta:
        model = Product
        fields = ['id', 'category', 'product_name', 'product_description', 'is_available', 'image_url']
