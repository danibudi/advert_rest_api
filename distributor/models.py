from django.db import models
from django.utils.translation import ugettext_lazy as _
from urlparse import urlparse


class Distributor(models.Model):
    name = models.CharField(max_length=200)
    show_percent = models.PositiveSmallIntegerField(
        default=100, blank=False, null=False)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name


class Advertisement(models.Model):
    distributor = models.ForeignKey(Distributor)
    banner = models.ImageField("Banner Image", upload_to='banner_immages/',
                               blank=False, null=False,
                               help_text='Please, upload gif, png format')
    banner_link = models.URLField(_("banner's URL"), blank=False, null=False)

    def __unicode__(self):              # __unicode__ on Python 2
        return urlparse(self.banner_link).path.split('/')[-1]
