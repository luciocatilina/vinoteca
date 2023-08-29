from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import WineForm, WineImageForm
from django.db import transaction
# Create your views here.

class FormCreateWine(CreateView):
    form_class = WineForm
    template_name='admin/form_wine.html'
    success_url='../store/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['image_formset'] = WineImageForm(self.request.POST, self.request.FILES)
        else:
            data['image_formset'] = WineImageForm()

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        with transaction.atomic():
            self.object = form.save()
            if image_formset.is_valid():
                image_formset.instance = self.object
                image_formset.save()
        return super(FormCreateWine, self).form_valid(form)