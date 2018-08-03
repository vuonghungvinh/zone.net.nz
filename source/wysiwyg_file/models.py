from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(
        upload_to='wysiwyg/%Y/%m/%d/',
        help_text='wysiwyg image')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.image.path