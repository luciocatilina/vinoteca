from django.contrib import admin
from django.http.request import HttpRequest
from .models import IndexLayout, IndexAbout

class IndexAdmin(admin.ModelAdmin):

    list_display=[
        'img_index',
        'h1_text',
        'p_text', 
    ]
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
class IndexAboutAdmin(admin.ModelAdmin):

    list_display = [
        'img_index_about',
        'h1_text',
        'p_text',
    ]
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

admin.site.register(IndexLayout, IndexAdmin)
admin.site.register(IndexAbout, IndexAboutAdmin)

