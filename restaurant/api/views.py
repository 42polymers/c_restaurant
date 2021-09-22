from rest_framework import generics

from .serializers import RestaurantSerializer
from .models import Restaurant


class RestaurantList(generics.ListCreateAPIView):
    """A view to get the list of restaurants/ create a restaurant"""

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save()


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    """A view to get/update/delete a restaurant by name """

    lookup_field = 'name'
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantGetRandom(generics.ListAPIView):
    """A view to get a random restaurant"""

    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.all().order_by('?')[:1]
