from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Post
from api.serializers import BlogSerializer

class PostViewSet(viewsets.ModelViewSet):
    """Listando todos os eventos"""
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['data_publicacao','titulo']
    search_fields = ['titulo']
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
