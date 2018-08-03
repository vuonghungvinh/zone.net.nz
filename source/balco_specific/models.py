from django.db import models

# Create your models here.

class PositionApplication(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Position / application'
        verbose_name_plural = 'Position / application'

    def __unicode__(self):
        return self.name


class InteriorExterior(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Interior / exterior'
        verbose_name_plural = 'Interior / exterior'

    def __unicode__(self):
        return self.name


class CoverType(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cover type'
        verbose_name_plural = 'Cover type'

    def __unicode__(self):
        return self.name


class GapWidth(models.Model):
    name = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gap width'
        verbose_name_plural = 'Gap width'

    def __unicode__(self):
        return str(self.name)


class Movement(models.Model):
    name = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Max joint movement'
        verbose_name_plural = 'Max joint movement'

    def __unicode__(self):
        return str(self.name)


FIELD_CHOICES = (
     (1, "Position / Application"),
     (2, "Interior / Exterior"),
     (3, "Cover Type"),
     (4, "Gap width"),
     (5, "Max Joint Movement"),
)

class ExplainationCopy(models.Model):
    content = models.TextField(null=True, blank=True)
    field = models.IntegerField(choices=FIELD_CHOICES, default=1, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('field',)
        verbose_name = 'Explanation box copy'
        verbose_name_plural = 'Explanation box copy'

    def __unicode__(self):
        return self.content