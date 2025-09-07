from django.core.management.base import BaseCommand
from agora_store.models import Collection, Product, ProductSize, ProductDetail, ProductDimension
from agora_store.data.products import products  # if you put the dataset in shop/data/products.py


class Command(BaseCommand):
    help = "Seed initial products into the database"

    def handle(self, *args, **options):
        for item in products:
            collection, _ = Collection.objects.get_or_create(
                name=item["collection"],
                slug=item["collection"].lower().replace(" ", "-"),
                defaults={"description": f"Collection: {item['collection']}"}
            )

            product, created = Product.objects.get_or_create(
                collection=collection,
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                    "old_price": item["oldPrice"],
                    "image": item["image"]
                }
            )

            # Sizes
            for size in item["sizes"]:
                ProductSize.objects.get_or_create(product=product, value=size)

            # Details
            for detail in item["details"]:
                ProductDetail.objects.get_or_create(product=product, value=detail)

            # Dimensions
            for dim in item["dimensions"]:
                ProductDimension.objects.get_or_create(product=product, value=dim)

        self.stdout.write(self.style.SUCCESS("Products seeded successfully!"))
