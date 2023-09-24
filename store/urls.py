from django.urls import path
from .views import ListWines
from .index_views import index


urlpatterns = [
    path('', index, name='index'),
    path('store', ListWines.as_view(), name='store'),
]

