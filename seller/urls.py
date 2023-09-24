from django.urls import path
from .views import FormCreateWine, FormUpdateWine

urlpatterns = [
    path('create_wine', FormCreateWine.as_view(), name='create_wine'),
    path('update_wine/<int:pk>', FormUpdateWine.as_view(), name='update_wine'),
]
