from django.contrib import admin
from .models import Variety, Grape, Cellar, Province, Wine, WineImage

admin.site.register(Variety)
admin.site.register(Grape)
admin.site.register(Cellar)
admin.site.register(Province)
admin.site.register(Wine)
admin.site.register(WineImage)

