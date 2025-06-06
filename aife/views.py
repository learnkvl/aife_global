from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Get list of categories
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Get list of products
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer

# Get details of a single product by ID
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
