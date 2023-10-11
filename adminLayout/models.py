from django.db import models
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from os.path import splitext

#REANAME IMGS-INDEX
def custom_upload_path_portada(_, filename):
    ext = splitext(filename)[1]
    new_filename = f'portada-img.{ext}'
    return f'gallery/{new_filename}'

def custom_upload_path_about(_, filename):
    ext = splitext(filename)[1]
    new_filename = f'about-img.{ext}'
    return f'gallery/{new_filename}'

#Remove old file from local
def remove_old_img(img_name):
    folder_path = os.path.abspath('media/gallery')
    list_files = os.listdir(folder_path)
    for i in list_files:
        if i.startswith(img_name):
            try:
                os.remove(f'{folder_path}/{img_name}')
            except:
                pass
################################################################
###################INDEX-PORTADA################################
################################################################
class IndexLayout(models.Model):
    img_index = models.ImageField(upload_to=custom_upload_path_portada, null=False, blank=False)
    h1_text = models.CharField(max_length=40, null=False, blank=False)
    p_text = models.TextField(null=False, blank=False)

    def __str__(self):
        return 'vinoteca-index'
################################################################
################################################################
################################################################

@receiver(pre_save, sender=IndexLayout)
def eliminar_archivo_anterior(sender, instance, **kwargs):
    if instance.pk:  # Verifica si la instancia ya existe en la base de datos (es una actualización)
        try:
            # Obtiene la instancia actual en la base de datos
            instancia_actual = sender.objects.get(pk=instance.pk)
            # Compara el campo1 de la instancia actual con la nueva instancia
            if instancia_actual.img_index != instance.img_index:
                # Elimina el archivo antiguo
                if instancia_actual.img_index:
                    os.remove(instancia_actual.img_index.path)
        except sender.DoesNotExist:
            pass
    remove_old_img('portada-img')
    
################################################################
#####################INDEX-ABOUT################################
################################################################
class IndexAbout(models.Model):
    img_index_about = models.ImageField(upload_to=custom_upload_path_about, null=False, blank=False)
    h1_text = models.CharField(max_length=40, null=False, blank=False)
    p_text = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return 'about-index'
################################################################
################################################################
################################################################

@receiver(pre_save, sender=IndexAbout)
def eliminar_archivo_anterior(sender, instance, **kwargs):
    if instance.pk:  # Verifica si la instancia ya existe en la base de datos (es una actualización)
        try:
            # Obtiene la instancia actual en la base de datos
            instancia_actual = sender.objects.get(pk=instance.pk)
            # Compara el campo1 de la instancia actual con la nueva instancia
            if instancia_actual.img_index_about != instance.img_index_about:
                # Elimina el archivo antiguo
                if instancia_actual.img_index_about:
                    os.remove(instancia_actual.img_index_about.path)
        except sender.DoesNotExist:
            pass
    remove_old_img('about-img')
