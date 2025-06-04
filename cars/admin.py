from django.contrib import admin

from cars.models import Car, Modification


# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'owner', 'region', 'created_at']
    list_filter = ['region', 'year', 'brand']
    search_fields = ['brand', 'model', 'owner__username']
    ordering = ['-created_at',]
    
@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'car', 'date_installed']
    list_filter = ['date_installed']
    search_fields = ['name', 'car__model', 'car__brand']

