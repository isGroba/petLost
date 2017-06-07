from django.contrib import admin

from .models import Color, Member, Pet, Publication


class PublicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'pet', 'location']
    search_fields = ['title', 'breed']

    list_display = ('title', 'description', 'pet', 'date', 'location')
    list_filter = ['date', 'location']


class PetAdmin(admin.ModelAdmin):
    fields = ['name', 'type_animal', 'breed', 'description', 'color']
    search_fields = ['name', 'breed']

    list_display = ('name', 'type_animal', 'breed', 'description')
    list_filter = ['type_animal', 'breed']


class ColorAdmin(admin.ModelAdmin):
    fields = ['name', 'code_color']
    search_fields = ['name']

    list_display = ('name', 'code_color')


class MemberAdmin(admin.ModelAdmin):
    fields = ['name', 'mail', 'phone', 'city']
    search_fields = ['name', 'city']

    list_display = ('name', 'mail', 'phone', 'city')


admin.site.register(Pet, PetAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Member, MemberAdmin)
