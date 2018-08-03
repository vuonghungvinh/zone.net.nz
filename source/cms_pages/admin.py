
from django.contrib import admin
from django.db import models
from django import forms

from .models import BasicPage, BasicImage, Page, Image, BasicFile, File
from widgets import RedactorTextarea


class PageForm(forms.ModelForm):
    """
    This form is specifically for providing Page instance inforation for the
    redactor settings. In this case the PK
    """
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

        # Get Entry Object Instance
        instance = kwargs.get('instance')

        # JSON Redactor settings
        settings = '{'
        settings += '"minHeight": "350"'
        if instance:
            settings += ', "imageGetJson": "/cms/images/json/{}/"'.format(instance.pk)
        settings += '}'

        self.fields['body'].widget = RedactorTextarea(attrs={'data-settings': settings})

    class Meta:
        model = Page


class ImageAdmin(admin.TabularInline):
    extra = 1
    model = Image
    verbose_name_plural = 'Images'


class FileAdmin(admin.TabularInline):
    extra = 1
    model = File
    verbose_name_plural = 'Files'


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ('name', 'section', 'order_link')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('section',)
    inlines = (ImageAdmin, FileAdmin,)


class BasicPageForm(forms.ModelForm):
    """
    This form is specifically for providing Basic Page instance inforation for the
    redactor settings. In this case the PK
    """
    def __init__(self, *args, **kwargs):
        super(BasicPageForm, self).__init__(*args, **kwargs)

        # Get Entry Object Instance
        instance = kwargs.get('instance')

        # JSON Redactor settings
        settings = '{'
        settings += '"minHeight": "350"'
        if instance:
            settings += ', "imageGetJson": "/cms/images/json/{}/"'.format(instance.pk)
        settings += '}'

        self.fields['body'].widget = RedactorTextarea(attrs={'data-settings': settings})

    class Meta:
        model = BasicPage


class BasicImageAdmin(admin.TabularInline):
    extra = 1
    model = BasicImage
    verbose_name_plural = 'Images'


class BasicFileAdmin(admin.TabularInline):
    extra = 1
    model = BasicFile
    verbose_name_plural = 'Files'


class BasicPageAdmin(admin.ModelAdmin):
    form = BasicPageForm
    inlines = (BasicImageAdmin, BasicFileAdmin,)
    settings = '{"minHeight": "300"}' # JSON string


admin.site.register(Page, PageAdmin)
admin.site.register(BasicPage, BasicPageAdmin)