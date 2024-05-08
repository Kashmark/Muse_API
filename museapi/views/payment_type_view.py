from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from museapi.models import PaymentType
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.http import Http404
from rest_framework import serializers


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ("id", "merchant_name", "number", "user")


class PaymentTypeViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """Handle GET requests to payment type resource"""
        payment_types = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(payment_types, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new payment type"""
        serializer = PaymentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single payment type"""
        try:
            payment_type = PaymentType.objects.get(pk=pk)
        except PaymentType.DoesNotExist:
            raise Http404
        serializer = PaymentTypeSerializer(payment_type)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests to update an existing payment type"""
        try:
            payment_type = PaymentType.objects.get(pk=pk)
        except PaymentType.DoesNotExist:
            raise Http404
        serializer = PaymentTypeSerializer(payment_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete an existing payment type"""
        try:
            payment_type = PaymentType.objects.get(pk=pk)
        except PaymentType.DoesNotExist:
            raise Http404
        payment_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
