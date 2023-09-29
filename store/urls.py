from django.urls import path
from .views import ListWines, get_list_wines
from .index_views import index, Inicio


urlpatterns = [
    path('', Inicio.as_view(), name='index'),
    path('store', ListWines.as_view(), name='store'),
    path('wines_data_json', get_list_wines)
]

