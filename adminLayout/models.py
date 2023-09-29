from django.db import models
import os
from django.db.models.signals import pre_save
from django.dispatch import receiver



class IndexLayout(models.Model):
    img_index = models.ImageField(upload_to='gallery', null=False, blank=False)
    h1_text = models.CharField(max_length=40, null=False, blank=False)
    p_text = models.TextField(null=False, blank=False)

    def __str__(self):
        return 'vinoteca-index'
    
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