from rest_framework import generics
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from .models import Order
from .serializers import OrderSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related("sizes", "details", "dimensions").select_related("collection")
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related("sizes", "details", "dimensions").select_related("collection")
    serializer_class = ProductSerializer


class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer