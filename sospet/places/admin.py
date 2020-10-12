from django.contrib import admin

from sospet.places.models import Places


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'description']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ['title','description']}
