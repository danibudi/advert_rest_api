from django.db import models
from django.utils.translation import ugettext_lazy as _
"""
from django.forms import IntegerField
from django.forms.widgets import Input
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal


https://djangosnippets.org/snippets/1914/
class PercentInput(Input):
    " A simple form input for a percentage "
    input_type = 'text'

    def _format_value(self, value):
        if value is None:
            return ''
        return str(int(value * 100))

    def render(self, name, value, attrs=None):
        value = self._format_value(value)
        return super(PercentInput, self).render(name, value, attrs)

    def _has_changed(self, initial, data):
        return super(PercentInput, self)._has_changed(self._format_value(initial), data)

class PercentField(IntegerField):
    " A field that gets a value between 0 and 1 and displays as a value between 0 and 100"
    widget = PercentInput(attrs={"class": "percentInput", "size": 4})

    default_error_messages = {
        'positive': _(u'Must be a positive number.'),
    }

    def clean(self, value):
        "Validates that the input can be converted to a value between 0 and 1. Returns a Decimal"
        value = super(PercentField, self).clean(value)
        if value is None:
            return None
        if (value < 0):
            raise ValidationError(self.error_messages['positive'])
        return Decimal("%.2f" % (value / 100.0))
"""

class Ditributor(models.Model):
    name = models.CharField(max_length=200)
    show_percent = models.PositiveSmallIntegerField(default=100, blank=False, null=False)

    def __unicode__(self):              # __unicode__ on Python 2
            return self.name

class Advertisement(models.Model):
    ditributor = models.ForeignKey(Ditributor)
    banner = models.ImageField("Banner Image", upload_to='banner_immages/', blank=False, null=False, help_text='Please, upload gif, png format')
    banner_link = models.URLField(_("banner's URL"), blank=False, null=False)
    thumbnail = models.ImageField(upload_to='doc100/', blank=False, null=False, editable=False)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.banner_link

    def save(self):
        if not self.thumbnail:
            # We use PIL's Image object
            # Docs: http://www.pythonware.com/library/pil/handbook/image.htm
            from PIL import Image
            from django.core.files.base import ContentFile

            # Set our max thumbnail size in a tuple (max width, max height)
            THUMBNAIL_SIZE = (300, 300)
            CROP_SIZE = (100, 100, 200, 200)

            # Save fake thumbnail as empty so we can get the filename from the
            # original filename, from Django's convenience method
            # get_FIELD_filename()
            self.thumbnail.save(self.banner.path, ContentFile(''))
            # Open original photo which we want to thumbnail using PIL's Image
            # object
            image = Image.open(self.banner.path)
            # Convert to RGB if necessary
            # Thanks to Limodou on DjangoSnippets.org
            # http://www.djangosnippets.org/snippets/20/
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')

            # We use our PIL Image object to create the thumbnail, which already
            # has a thumbnail() convenience method that contrains proportions.
            # Additionally, we use Image.ANTIALIAS to make the image look better.
            # Without antialiasing the image pattern artifacts may result.
            image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
            image = image.crop(CROP_SIZE)

            # Save the thumbnail
            image.save(self.thumbnail.path)

        # Save this photo instance
        super(Advertisement, self).save()
