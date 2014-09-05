from django.contrib import admin
from distributor.models import Distributor, Advertisement


class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    extra = 3
    list_display = ('banner', 'banner_link')


def make_percent_proportionally(modeladmin, request, queryset):
    queryset = Distributor.objects.all()
    total_percents = 0
    for p in queryset:
        total_percents += p.show_percent
    proportional_coef = total_percents / 100.00
    for p in queryset:
        p.show_percent = round(p.show_percent / proportional_coef)
        p.save()
make_percent_proportionally.short_description = "Make percents in the right proportion"

"""
def make_percent_proportionally_button():
    queryset = Distributor.objects.all()
    total_percents = 0
    for p in queryset:
        total_percents += p.show_percent
    proportional_coef = total_percents / 100.00
    for p in queryset:
        p.show_percent = round(p.show_percent / proportional_coef)
        p.save()
"""

class DistributorAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline]
    list_display = ('name', 'show_percent', 'shown_adverts')
    list_filter = ['show_percent']
    search_fields = ['name']
    list_editable = ['show_percent']
    actions = [make_percent_proportionally]

    #~ change_list_template = 'distributor/admin/change_form.html'


admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Advertisement)
