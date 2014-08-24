from django.contrib import admin
from ditributor.models import Ditributor, Advertisement


class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    extra = 3
    list_display = ('banner', 'banner_link')


class DitributorAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline]
    list_display = ('name', 'show_percent')
    list_filter = ['show_percent']
    search_fields = ['name']

admin.site.register(Ditributor, DitributorAdmin)
admin.site.register(Advertisement)
