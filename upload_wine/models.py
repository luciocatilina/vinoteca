from django.db import models

class Variety(models.Model):  
    red = 'Red'
    white = 'White'
    pink = 'Pink'
    sparkling = 'Sparkling'
    #Select
    varieties = [
        #[0]k, [1]v
        (red, 'Tinto'),
        (white, 'Blanco'),
        (pink, 'Rosado'),
        (sparkling, 'Espumoso'),
    ]
    #-
    variety=models.CharField(
        max_length=9,
        choices=varieties,
    )
class Grape(models.Model):
    malbec = 'Malbec'
    chardonnay = 'Chardonnay'
    cabernet_sauvignon = 'Cabernet Sauvignon'
    bonarda = 'Bonarda'
    #Select
    grapes= [
        (malbec, 'Malbec'),
        (chardonnay, 'Chardonnay'),
        (cabernet_sauvignon, 'Cabernet Sauvignon'),
        (bonarda, 'Bonarda'),
    ]
    #-
    grape=models.CharField(
        max_length=25,
        choices=grapes,
    )

class Cellar(models.Model):
    #Select
    cellars= [
        ('Bodega_del_Valle', 'Bodega del Valle'),
        ('Bodega_Sol_Radiante', 'Bodega Sol Radiante'),
        ('Bodega_de_los_Andes', 'Bodega de los Andes'),
        ('Bodega_de_la_Brisa', 'Bodega de la Brisa'),
        ('Bodega_Aurora', 'Bodega Aurora'),
        ('Bodega_Vientos_del_Sur', 'Bodega Vientos del Sur'),
        ('Bodega_Sonora', 'Bodega Sonora'),
        ('Bodega_Lunaria', 'Bodega Lunaria'),
        ('Bodega_de_los_Sueños', 'Bodega de los Sueños'),
        ('Bodega_Eufórica', 'Bodega Eufórica'),
    ]
    #-
    cellar = models.CharField(
        max_length=50,
        choices=cellars,
    )

class Province(models.Model):
    #Select
    provinces = [
        ('Mendoza', 'Mendoza'),
        ('Neuquen', 'Neuquen'),
        ('La_Rioja', 'La Rioja'),
        ('San_Juan', 'San Juan'),
        ('Salta', 'Salta'),
    ]
    #-
    province = models.CharField(
        max_length=10,
        choices=provinces
    )

class Wine(models.Model):

    name=models.CharField(max_length=50, null=False, blank=False)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, null=False, blank=False)
    grape = models.ForeignKey(Grape, on_delete=models.CASCADE, null=False, blank=False)
    cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, null=False, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=False, blank=False)
    year=models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

class Photo(models.Model):
    wine_id = models.ForeignKey(Wine, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to= 'wine_photos', null=False, blank=False)