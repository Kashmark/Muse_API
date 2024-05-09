from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from museapi.models import Order
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.http import Http404
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "payment_type", "user", "created_date")


class OrderViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """Handle GET requests to order resource"""
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new order"""
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single order"""
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests to update an existing order"""
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete an existing order"""
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
