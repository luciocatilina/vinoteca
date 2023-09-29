from django.shortcuts import render
from adminLayout.models import IndexLayout
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

class Inicio(ListView):

    model = IndexLayout

    template_name = 'index.html'
