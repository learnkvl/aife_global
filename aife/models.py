from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    categories = models.ManyToManyField(Category, related_name='multi_category_products', blank=True)

    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    badge = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}: {self.value}"

  

# QUICK ENQUIRY
class QuickEnquiry(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry by {self.name}"
