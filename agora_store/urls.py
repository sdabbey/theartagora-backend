from django.urls import path
from .views import OrderCreateView

from .views import ProductListView, ProductDetailView, CollectionListView, ArtistOnboardingCreateView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("collections/", CollectionListView.as_view(), name="collection-list"),
    path("checkout/", OrderCreateView.as_view(), name="checkout"),
    path("artists/onboarding/", ArtistOnboardingCreateView.as_view(), name="artist-onboarding"),
]



