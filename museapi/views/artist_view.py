from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from museapi.models import Artist, Medium
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = ("id", "type")


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    preferred_medium = MediumSerializer()

    class Meta:
        model = Artist
        fields = ("id", "user", "bio", "preferred_medium")


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]
