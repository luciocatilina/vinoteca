from django.shortcuts import render
from .models import IndexLayout, IndexAbout
from django.http import JsonResponse

def index_data(request):
    #portada
    data_portada = IndexLayout.objects.first()
    portada, titulo, parrafo = data_portada.img_index, data_portada.h1_text, data_portada.p_text

    #about
    data_about = IndexAbout.objects.first()
    foto_ab, titulo_ab, parrafo_ab = data_about.img_index_about, data_about.h1_text, data_about.p_text

    if portada and foto_ab:
        data = {
            'message': 'Success',
            'portada': [portada.url, titulo, parrafo],
            'about' : [foto_ab.url, titulo_ab, parrafo_ab]
        }
    else:
        data = {
            'message': 'Error'
        }
    
    return JsonResponse(data)