from django.db import models


class Collection(models.Model):
    """A group of related products (e.g. Signature Collection)."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.name

class Product(models.Model):
    """Product model for Art Agora shop."""
    collection = models.ForeignKey(Collection, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name="sizes", on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - {self.value}"


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name="details", on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.value}"


class ProductDimension(models.Model):
    product = models.ForeignKey(Product, related_name="dimensions", on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.value}"

#Order Models
class Order(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=3)  # ISO code
    phoneNumber = models.CharField(max_length=20)
    instructions = models.TextField(blank=True, null=True)
    subscribe = models.BooleanField(default=False)
    totalPrice = models.CharField(max_length=10)
    is_paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.email}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Order {self.order.id})"
    

class ArtistOnboarding(models.Model):
    alias = models.CharField(max_length=150)  # your “Artist Alias”
    email = models.EmailField()
    display_name = models.CharField(max_length=255)
    bio = models.TextField()
    portfolio_url = models.URLField(blank=True, null=True)
    preferred_medium = models.CharField(max_length=120, blank=True)
    agree_to_terms = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.alias})"
