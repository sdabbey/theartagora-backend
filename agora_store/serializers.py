from rest_framework import serializers
from django.templatetags.static import static
from .models import Collection, Product, ProductSize, ProductDetail, ProductDimension, Order, OrderItem


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name", "description", "slug", "created_at"]


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["id", "value"]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ["id", "value"]


class ProductDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDimension
        fields = ["id", "value"]


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(read_only=True)
    collection_id = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all(), source="collection", write_only=True
    )
    sizes = ProductSizeSerializer(many=True, read_only=True)
    details = ProductDetailSerializer(many=True, read_only=True)
    dimensions = ProductDimensionSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "image",
            "price",
            "old_price",
            "collection",
            "collection_id",
            "sizes",
            "details",
            "dimensions",
            "created_at",
        ]

    def get_image(self, obj):
        request = self.context.get("request")  # comes from the view
        if obj.image:
            url = static(f"{obj.image}")  # relative: /static/products/tote_bag.png
            if request is not None:
                return request.build_absolute_uri(url)  # absolute: https://yourdomain.com/static/products/tote_bag.png
            return url
        return None


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["product_id", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "email",
            "firstName",
            "lastName",
            "address",
            "apartment",
            "city",
            "totalPrice",
            "postalCode",
            "country",
            "phoneNumber",
            "instructions",
            "subscribe",
            "is_paid",
            "payment_reference",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(
                order=order,
                product_id=item["product_id"],
                quantity=item["quantity"],
                price=item["price"],
            )
        return order