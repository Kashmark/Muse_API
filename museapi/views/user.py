from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, pk=None):
        """Handle DELETE requests to user resource"""
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully"})
