from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """The restaurant serializer"""

    class Meta:
        model = Restaurant
        fields = ['name']
