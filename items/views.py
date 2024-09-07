from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication

class ItemPagination(PageNumberPagination):
    page_size = 5

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ItemPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        serializer.save()

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the API!")
