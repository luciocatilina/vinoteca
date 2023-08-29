from django.urls import path
from .views import ListWines


urlpatterns = [
    path('', ListWines.as_view(), name='store')
]

