from rest_framework import generics
from .models import Product, Collection, Order, ArtistOnboarding
from .serializers import ProductSerializer, CollectionSerializer, OrderSerializer, ArtistOnboardingSerializer
from django.core.mail import send_mail
from django.conf import settings



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


class ArtistOnboardingCreateView(generics.CreateAPIView):
    queryset = ArtistOnboarding.objects.all()
    serializer_class = ArtistOnboardingSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            send_mail(
                subject="New Artist Onboarding Submission",
                message=(
                    f"Alias: {instance.alias}\n"
                    f"Name: {instance.display_name}\n"
                    f"Email: {instance.email}\n"
                    f"Medium: {instance.preferred_medium}\n"
                    f"Portfolio: {instance.portfolio_url}\n\n"
                    f"Bio:\n{instance.bio}"
                ),
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
                recipient_list=[ "samueldarko557@gmail.com" ],  # put your email here
                fail_silently=True,
            )
        except Exception:
            pass