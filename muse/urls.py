from django.contrib import admin
from django.urls import path, include
from museapi.views import (
    ArtistViewSet,
    MediumViewSet,
    ArtworkViewSet,
    register_user,
    login_user,
    CategoryViewSet,
    ArtCategoryViewSet,
    OrderArtworkViewSet,
    OrderViewSet,
    PaymentTypeViewSet,
    UserViewSet,
)
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"artists", ArtistViewSet, basename="artist")
router.register(r"mediums", MediumViewSet, basename="medium")
router.register(r"artworks", ArtworkViewSet, basename="artworks")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"artworkCategory", ArtCategoryViewSet, basename="ArtCategories")
router.register(r"orderArtworks", OrderArtworkViewSet, basename="orderArtwork")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"paymentTypes", PaymentTypeViewSet, basename="paymentTypes")
router.register(r"users", UserViewSet, basename="users")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("register/", register_user),
    path("login/", login_user),
    path("api-token-auth/", obtain_auth_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
