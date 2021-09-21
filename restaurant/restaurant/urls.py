from django.urls import include, path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='ooo')

urlpatterns = [
    path('', schema_view),
    path('', include('api.urls')),
]
