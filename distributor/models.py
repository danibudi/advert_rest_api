from django.db import models
from django.utils.translation import ugettext_lazy as _
from urlparse import urlparse


class Distributor(models.Model):
    name = models.CharField(max_length=200)
    show_percent = models.PositiveSmallIntegerField(
        default=100, blank=False, null=False)
    shown_adverts = models.PositiveSmallIntegerField(
        default=0, blank=False, null=False)

    def __unicode__(self):              # __str__ on Python 3
            return self.name


class Advertisement(models.Model):
    distributor = models.ForeignKey(Distributor)
    banner = models.ImageField("Banner Image", upload_to='banner_immages/',
                               blank=False, null=False,
                               help_text='Please, upload gif, png format')
    banner_link = models.URLField(_("banner's URL"), blank=False, null=False)

    def __unicode__(self):              # __str__ on Python 3
        return urlparse(self.banner_link).path.split('/')[-1]


def make_dist_adv_list():
    #~ prepare list like
    #~ distr_percent_advs_list = [('b', 10, [2, 4, 6, 7]),
                               #~ ('a', 70, [1, 5, 8]),
                               #~ ('c', 20, [9, 10, 11, 12])]
    distr_percent_advs_list = []
    distributors = Distributor.objects.all()
    for dist in distributors:
        adverts_distr_list = [adv.id for adv in dist.advertisement_set.all()]
        distr_percent_advs_list.append(
            (dist.name, dist.show_percent, adverts_distr_list))
    return distr_percent_advs_list
