from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', login, name='login'),
    path('register', registration, name='registration'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
]

