from rest_framework import serializers
from .models import Category, Software

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = ('__all__')