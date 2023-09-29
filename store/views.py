from django.shortcuts import render
from django.views.generic.list import ListView
from seller.models import Wine, WineImage
from django.http import JsonResponse

# Create your views here.

class ListWines(ListView):
    model=Wine
    template_name='store/list_wines.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.all().order_by('-pk')
    
    def get_context_data(self, **kwargs):
        context = super(ListWines, self).get_context_data(**kwargs)
        list_ids_wines = Wine.objects.all().values_list('id', flat=True)
        images = list()
        for i in list_ids_wines:
            if WineImage.objects.select_related('wine').filter(wine_id = i): #wine --> Main Model ///wine_id --> registro model fk (child)
                images.append(WineImage.objects.select_related('wine').filter(wine_id = i)[0])
                context['images'] = images
        return context
    
def get_list_wines(request):

    list_wines = list(Wine.objects.values())

    for i in range(len(list_wines)):
        img = WineImage.objects.filter(wine_id = list_wines[i]['id']).first().photo.url #cuando se trabaja con img siempre poner first(). wine_id es el registro fk, 
        list_wines[i]['img'] = img

    if len(list_wines) > 0:
        data = {'message' : 'Success', 'wines' : list_wines}
    else: 
        data = {'message' : 'Error'}
    return JsonResponse(data)