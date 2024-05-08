from rest_framework.viewsets import ModelViewSet
from museapi.models import OrderArtwork, Order
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import serializers
from museapi.views import ArtworkSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "payment_type", "user", "created_date")


class OrderArtworkCreateSerializer(serializers.ModelSerializer):

    # order = OrderSerializer()
    # artwork = ArtworkSerializer()

    class Meta:
        model = OrderArtwork
        fields = ("id", "artwork", "order")


class OrderArtworkSerializer(serializers.ModelSerializer):

    order = OrderSerializer()
    artwork = ArtworkSerializer()

    class Meta:
        model = OrderArtwork
        fields = ("id", "artwork", "order")


class OrderArtworkViewSet(ModelViewSet):
    queryset = OrderArtwork.objects.all()
    serializer_class = OrderArtworkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single order artwork"""
        try:
            order_artwork = self.get_object()
        except OrderArtwork.DoesNotExist:
            raise Http404
        serializer = OrderArtworkSerializer(order_artwork)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new order artwork"""
        serializer = OrderArtworkCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests to update an existing order artwork"""
        order_artwork = self.get_object()
        serializer = OrderArtworkSerializer(order_artwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete an existing order artwork"""
        order_artwork = self.get_object()
        order_artwork.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
