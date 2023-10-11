from django.urls import path
from .views import index_data

urlpatterns = [
    path('index_data_json', index_data)
]
