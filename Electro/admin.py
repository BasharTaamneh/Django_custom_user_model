from django.contrib import admin
from .models import Electro

class ElectroAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Electro, ElectroAdmin)
