from django.contrib import admin
from agora_store.models import Collection, Product, ProductSize, ProductDetail, ProductDimension, Order, OrderItem

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductDetail)
admin.site.register(ProductDimension)
admin.site.register(Order)
admin.site.register(OrderItem)

