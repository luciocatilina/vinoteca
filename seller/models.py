from django.db import models

class Variety(models.Model):  
    RED = 'Red'
    WHITE = 'White'
    PINK = 'Pink'
    SPARKLING = 'Sparkling'
    
    varieties = [
        #[0]k, [1]v
        (RED, 'Tinto'),
        (WHITE, 'Blanco'),
        (PINK, 'Rosado'),
        (SPARKLING, 'Espumoso'),
    ]
    #-
    variety=models.CharField(
        max_length=9,
        choices=varieties,
        default=RED,
    )

    def __str__(self) -> str:
        return self.get_variety_display()




class Grape(models.Model):
    MALBEC = 'Malbec'
    CHARDONNAY = 'Chardonnay'
    CABERNET_SAUVIGNON = 'CabernetSauvignon'
    BONARDA = 'Bonarda'
    #Select
    grapes= [
        (MALBEC, 'Malbec'),
        (CHARDONNAY, 'Chardonnay'),
        (CABERNET_SAUVIGNON, 'Cabernet Sauvignon'),
        (BONARDA, 'Bonarda'),
    ]
    #-
    grape=models.CharField(
        max_length=25,
        choices=grapes,
    )

    def __str__(self) -> str:
        return self.get_grape_display()

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
        ('Bodega_de_los_Suenos', 'Bodega de los Sueños'),
        ('Bodega_Euforica', 'Bodega Eufórica'),
    ]
    #-
    cellar = models.CharField(
        max_length=50,
        choices=cellars,
    )
    def __str__(self) -> str:
        return self.get_cellar_display()

class Province(models.Model):
    MENDOZA = 'Mendoza'
    NEUQUEN = 'Neuquen'
    LA_RIOJA = 'La_Rioja'
    SAN_JUAN = 'San_Juan'
    SALTA = 'Salta'

    provinces = [
        (MENDOZA, 'Mendoza'),
        (NEUQUEN, 'Neuquen'),
        (LA_RIOJA, 'La Rioja'),
        (SAN_JUAN, 'San Juan'),
        (SALTA, 'Salta'),
    ]
    #-
    province = models.CharField(
        max_length=10,
        choices=provinces,
    )
    def __str__(self) -> str:
        return self.get_province_display()

class Wine(models.Model):

    name=models.CharField(max_length=50, null=False, blank=False)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, null=False, blank=False,)    
    grape = models.ForeignKey(Grape, on_delete=models.CASCADE, null=False, blank=False,)
    cellar = models.ForeignKey(Cellar, on_delete=models.CASCADE, null=False, blank=False,)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=False, blank=False,)
    year=models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __srt__(self):
        return self.name

class WineImage(models.Model):
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to= 'wine_photos', null=False, blank=False)
