from django.shortcuts import render
from django.views.generic.list import ListView
from upload_wine.models import Wine, WineImage

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