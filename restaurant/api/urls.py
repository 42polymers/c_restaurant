from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view(), name='restaurants'),
    path('restaurants/<str:name>/', views.RestaurantDetail.as_view(),
         name='restaurants_details'),
    path('restaurants_random/', views.RestaurantGetRandom.as_view(),
         name='restaurants_random')
]

urlpatterns = format_suffix_patterns(urlpatterns)