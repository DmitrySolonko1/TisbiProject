from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'description', 'marketplace', 'price']
    list_display_links = ['title', 'description', 'marketplace', 'price']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="70px" height="70px"')
        else:
            return '-'

    get_image.shortcut_description = 'Изображение'


admin.site.register(Product, ProductAdmin)
admin.site.register(Deal)
admin.site.register(Payment)
admin.site.register(Marketplace)
admin.site.register(ProductType)
