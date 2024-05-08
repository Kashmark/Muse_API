from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from museapi.models import Medium
from rest_framework import serializers
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)  # Import the permission class


class MediumSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Medium"""

    class Meta:
        model = Medium
        fields = ("id", "type")


class MediumViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """Handle GET requests to medium resource"""
        mediums = Medium.objects.all()
        serializer = MediumSerializer(mediums, many=True)
        return Response(serializer.data)
