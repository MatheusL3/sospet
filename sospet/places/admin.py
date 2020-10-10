from django.contrib import admin

from sospet.places.models import Places


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']