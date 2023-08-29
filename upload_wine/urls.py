from django.urls import path
from .views import FormCreateWine

urlpatterns = [
    path('form_wine', FormCreateWine.as_view(), name='form_creation_wine')
]
