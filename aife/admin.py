from django.contrib import admin
from .models import Category, Product, ProductSpec, QuickEnquiry
from accounts.models import Customer  # assuming you have this

# 🌐 Customizing the Admin Panel Branding
admin.site.site_header = 'A IS FOR EVERYTHING ADMIN'
admin.site.site_title = 'A IS FOR EVERYTHING'
admin.site.index_title = 'Welcome to A IS FOR EVERYTHING'

# 🏷️ Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}  # optional, auto-generates slug from name

# 🧾 Inline for Product Specifications
class ProductSpecInline(admin.TabularInline):
    model = ProductSpec
    extra = 1

# 📦 Product admin
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'category', 'product_name', 'product_description', 'is_available', 'image_url'
    )
    list_filter = ('category', 'is_available')
    search_fields = ('product_name', 'product_description')
    inlines = [ProductSpecInline]
    filter_horizontal = ('categories',)

# ✉️ QuickEnquiry admin
class QuickEnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    readonly_fields = ('created_at',)

# ✅ Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(QuickEnquiry, QuickEnquiryAdmin)

