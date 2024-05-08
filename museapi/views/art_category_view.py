from rest_framework import viewsets, status
from rest_framework.response import Response
from museapi.models import ArtCategory
from rest_framework import serializers


class ArtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtCategory
        fields = "__all__"


class ArtCategoryViewSet(viewsets.ViewSet):
    queryset = ArtCategory.objects.all()
    serializer_class = ArtCategorySerializer

    def list(self, request):
        queryset = ArtCategory.objects.all()
        serializer = ArtCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArtCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            category = ArtCategory.objects.get(pk=pk)
        except ArtCategory.DoesNotExist:
            return Response(
                {"message": "ArtCategory not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ArtCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
