from django import forms
from .models import Wine, WineImage
from django.forms import inlineformset_factory


class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = '__all__'

        labels = {
            'name' : 'Nombre',
            'variety': 'Tipo',
            'grape' : 'Cepa',
            'cellar' : 'Bodega',
            'year' : 'Año de elaboración',
            'description' : 'Descripción',
            'price'  : 'Precio',
            'province' : 'Provincia',
        }


class WineImageForm(forms.ModelForm):

    class Meta:
        model = WineImage
        fields = ['photo']



WineImageForm = inlineformset_factory(
    Wine, WineImage,
    fields=['photo'],
    labels= {'photo' : 'Foto'},
    extra=1,
    can_delete=False
)