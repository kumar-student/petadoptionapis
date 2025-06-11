from django.contrib import admin
from django.utils.safestring import mark_safe

from adoption.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'owner_name', 'owner_email']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"

    image_preview.short_description = 'Image Preview'

admin.site.register(Pet, PetAdmin)
