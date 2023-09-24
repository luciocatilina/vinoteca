from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import WineForm, WineImageForm
from .models import Wine
from django.db import models, transaction


#Create wine
class FormCreateWine(CreateView):
    form_class = WineForm
    template_name='seller/create_wine.html'
    success_url='../store/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['wine_formset'] = WineImageForm(self.request.POST, self.request.FILES)
        else:
            data['wine_formset'] = WineImageForm()

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        wine_formset = context['wine_formset']
        with transaction.atomic():
            self.object = form.save()
            if wine_formset.is_valid():
                wine_formset.instance = self.object
                wine_formset.save()
        return super(FormCreateWine, self).form_valid(form)
#end create

#Update Wine
class FormUpdateWine(UpdateView):
    model = Wine
    form_class = WineForm
    template_name='seller/update_wine.html'
    success_url= reverse_lazy('store')

    def get_queryset(self, **kwargs):
        
        return Wine.objects.filter(pk = self.kwargs['pk'])
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['wine_formset'] = WineImageForm(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['wine_formset'] = WineImageForm()

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        wine_formset = context['wine_formset']
        with transaction.atomic():
            self.object = form.save()
            if wine_formset.is_valid():
                wine_formset.instance = self.object
                wine_formset.save()
        return super().form_valid(form)
#end create