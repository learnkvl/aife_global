# from rest_framework import serializers
# from .models import Category, Product

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()  # To return full category object

#     class Meta:
#         model = Product
#         fields = ['id', 'category', 'product_name', 'product_description', 'is_available', 'image_url']

from rest_framework import serializers
from .models import Product, ProductSpec, Category

class ProductSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpec
        fields = ['label', 'value']

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source='product_name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    image = serializers.CharField(source='image_url')
    description = serializers.CharField(source='product_description')
    specs = ProductSpecSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'categories', 'image', 'badge', 'description', 'specs']

