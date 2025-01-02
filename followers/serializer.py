from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Follower
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':' possible duplicated'
            })
