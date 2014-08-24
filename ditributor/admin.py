from django.contrib import admin
from ditributor.models import Ditributor, Advertisement


class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    extra = 3
    list_display = ('banner', 'banner_link')


def make_percent_proportionally(modeladmin, request, queryset):
    queryset = Ditributor.objects.all()
    total_percents = 0
    for p in queryset:
        total_percents += p.show_percent
    proportional_coef = total_percents / 100.00
    for p in queryset:
        p.show_percent = round(p.show_percent / proportional_coef)
        p.save()
make_percent_proportionally.short_description = "Make percents in the right proportion"


class DistributorAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline]
    list_display = ('name', 'show_percent')  #, 'percent'
    list_filter = ['show_percent']
    search_fields = ['name']
    list_editable = ['show_percent']
    actions = [make_percent_proportionally]



admin.site.register(Ditributor, DistributorAdmin)
admin.site.register(Advertisement)
