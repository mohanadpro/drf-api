from django.shortcuts import render
from .models import Software, Category
from rest_framework import generics
from .serializers import CategorySerializer, SoftwareSerializer
# Create your views here.
class CategoryList(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SoftwareList(generics.CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
