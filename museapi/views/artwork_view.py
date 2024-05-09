from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from museapi.models import Artwork, Artist, Medium
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from django.http import Http404
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email")


class MediumSerializer(ModelSerializer):
    class Meta:
        model = Medium
        fields = ("id", "type")


class ArtistSerializer(ModelSerializer):
    user = UserSerializer()
    preferred_medium = MediumSerializer()

    class Meta:
        model = Artist
        fields = (
            "id",
            "user",
            "bio",
            "preferred_medium",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email")


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ("id", "type")


class ArtworkSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source="artist", write_only=True
    )
    medium_id = serializers.PrimaryKeyRelatedField(
        queryset=Medium.objects.all(), source="medium", write_only=True
    )
    artist = ArtistSerializer(read_only=True)
    medium = MediumSerializer(read_only=True)

    class Meta:
        model = Artwork
        fields = (
            "id",
            "price",
            "artist_id",
            "medium_id",
            "artist",
            "medium",
            "picture_url",
            "description",
        )


class ArtworkViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        """Handle GET requests to artwork resource"""
        artworks = Artwork.objects.all()
        serializer = ArtworkSerializer(artworks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new artwork"""
        serializer = ArtworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests to retrieve a single artwork"""
        try:
            artwork = Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            raise Http404
        serializer = ArtworkSerializer(artwork)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests to update an existing artwork"""
        try:
            artwork = Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            raise Http404
        serializer = ArtworkSerializer(artwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to delete an existing artwork"""
        try:
            artwork = Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            raise Http404
        artwork.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
