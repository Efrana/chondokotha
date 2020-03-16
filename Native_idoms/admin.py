from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name','bn_name']

admin.site.register(Division, DivisionAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','bn_name','division','lat','lon']

admin.site.register(District, DistrictAdmin)

class ChondokothaAdmin(admin.ModelAdmin):
    list_display = ['title','district','category_name','district_name','division_name']

admin.site.register(Chondokotha, ChondokothaAdmin)