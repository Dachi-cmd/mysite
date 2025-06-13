from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Planet

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_days', 'distance_from_sun', 'has_rings')
    search_fields = ('name',)
    list_filter = ('has_rings',)

admin.site.register(Planet, PlanetAdmin)

