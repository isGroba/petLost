from django.contrib import admin

from .models import Color, Pet, Publication


class PublicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'pet', 'member']
    search_fields = ['title', 'breed']

    list_display = ('title', 'description', 'pet', 'date')
    list_filter = ['date']


class PetAdmin(admin.ModelAdmin):
    fields = ['name', 'type_animal', 'breed', 'description', 'color', 'picture', 'location']
    search_fields = ['name', 'breed']

    list_display = ('name', 'type_animal', 'breed', 'description', 'location')
    list_filter = ['type_animal', 'breed']


class ColorAdmin(admin.ModelAdmin):
    fields = ['name', 'code_color']
    search_fields = ['name']

    list_display = ('name', 'code_color')


admin.site.register(Pet, PetAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Color, ColorAdmin)
