from django.contrib import admin
from django.http.request import HttpRequest
from .models import IndexLayout

class IndexAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

admin.site.register(IndexLayout)


