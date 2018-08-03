import os

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

from . import ordered_model

from animal3.search import TinySearch
from balco_specific.models import PositionApplication, InteriorExterior, CoverType, GapWidth, Movement


class BaseCategory(ordered_model.OrderedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        verbose_name='URL Fragment',
        help_text='Suggested value generated from name.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('order',)

    def __unicode__(self):
        return self.name


class Category(BaseCategory):
    page_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Page Title')
    meta_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Page Meta',
        help_text='Set Meta Description for this page.')
    logo = models.ImageField(
        verbose_name='Pull Down Menu Logo',
        upload_to='catalogue/%Y/%m/%d',
        help_text='Logo will be shown as-is with no scaling',
        blank=True)
    main_logo = models.ImageField(
        verbose_name='Main Logo',
        upload_to='catalogue/%Y/%m/%d',
        help_text='Logo will be shown as-is with no scaling',
        null=True,
        blank=True)
    colour_ranges = models.ManyToManyField('colours.Range', blank=True)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse(
            'catalogue-category-detail',
            kwargs={'slug': self.slug, 'pk': self.pk})


class CategoryImage(models.Model):
    image = models.ImageField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add extra images to this category.')
    category = models.ForeignKey(
        Category,
        related_name='category_images')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.image.path


class CategoryFile(models.Model):
    file = models.FileField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add files to this category.')
    category = models.ForeignKey(
        Category,
        related_name='category_files')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.file.path


class SubCategory(BaseCategory):
    page_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Page Title')
    meta_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Page Meta',
        help_text='Set Meta Description for this page.')
    category = models.ForeignKey(
        Category,
        related_name='sub_categories')
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Sub Categories'


    def get_absolute_url(self):
        return reverse(
            'catalogue-sub-category-detail',
            kwargs={'category_slug': self.category.slug, 'slug': self.slug,
                'pk': self.pk})


class Group(BaseCategory):
    sub_category = models.ForeignKey(
        SubCategory,
        related_name='groups')

    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Product Groups'

    def get_class(self):
        return '{}'.format(self.__class__)


class ProductManager(models.Manager):
    def search(self, query):
        fields = {'name': 5, 'description': 1}
        queryset = self.get_query_set().select_related('brand')
        searcher = TinySearch(queryset, fields)
        return searcher.search(query).most_common()


class ProductGapWidth(ordered_model.OrderedModel):
    name = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=255,
        verbose_name='URL Fragment',
        help_text='Suggested value generated from name.')
    cover_image = models.ImageField(
        upload_to='catalogue/%Y/%m/%d',
        help_text='Cover Image for this product.',
        blank=True)
    excerpt = models.TextField(
        blank=True,)
    description = models.TextField()
    gap_width = models.CharField(
        max_length=255,
        help_text="Gap width (mm)")
    movement = models.IntegerField(
        blank=True,
        help_text="Movement (%) assigned to gap width")
    gap_width_finder = models.ForeignKey(
        GapWidth,
        null=True,
        blank=True,
        verbose_name='Gap width (mm)',
        related_name='gap_widths')
    movement_finder = models.ForeignKey(
        Movement,
        null=True,
        blank=True,
        verbose_name='Max Joint Movement (%)',
        related_name='movements')
    position_application = models.ManyToManyField(
        PositionApplication,
        null=True,
        blank=True,
        verbose_name='Position / Application',
        related_name='position_applications')
    interior_exterior = models.ManyToManyField(
        InteriorExterior,
        null=True,
        blank=True,
        verbose_name='Interior / Exterior',
        related_name='interior_exteriors')
    cover_type = models.ForeignKey(
        CoverType,
        null=True,
        blank=True,
        verbose_name='Cover Type',
        related_name='cover_types')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    class Meta:
        ordering = ('order',)
        verbose_name = 'Balco Product'
        verbose_name_plural = 'Balco Products'

    def get_absolute_url(self):
        return reverse(
            'catalogue-product-detail',
            kwargs={'slug': self.slug, 'pk': self.pk})

    def get_class(self):
        return '{}'.format(self.__class__)

    def __unicode__(self):
        return self.name


class Product(ordered_model.OrderedModel):
    sub_category = models.ForeignKey(
        SubCategory,
        related_name='products')
    group = models.ManyToManyField(
        Group,
        blank=True,
        help_text='Available groups will be filtered by sub category after the product has been saved for the first time.',)
    gapwidth = models.ManyToManyField(
        ProductGapWidth,
        null=True,
        blank=True,
        related_name='gapwidth_products',
        help_text='Product gap widths.',)
    related_products = models.ManyToManyField(
        'Product',
        blank=True)
    colour_ranges = models.ManyToManyField(
        'colours.Range',
        blank=True)
    projects = models.ManyToManyField(
        'projects.Entry',
        blank=True)
    featured = models.BooleanField(
        default=False,
        help_text='Featured products will be show on the homepage.')
    name = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=255,
        verbose_name='URL Fragment',
        help_text='Suggested value generated from name.')
    page_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Page Title',
        help_text='Page title will include product name and sub title by default.')
    sub_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Sub Title')
    meta_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Page Meta',
        help_text='Meta description will be sourced from product description by default.')
    cover_image = models.ImageField(
        upload_to='catalogue/%Y/%m/%d',
        help_text='Cover Image for this product.',
        blank=True)
    excerpt = models.TextField(
        blank=True,)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    class Meta:
        ordering = ('order',)

    def get_absolute_url(self):
        return reverse(
            'catalogue-product-detail',
            kwargs={'slug': self.slug, 'pk': self.pk})

    def get_class(self):
        return '{}'.format(self.__class__)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add images to this product.')
    name = models.CharField(
        max_length=255,
        blank=True)
    caption = models.TextField(
        blank=True)
    product = models.ForeignKey(
        Product,
        related_name='images')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.image.path


class File(ordered_model.OrderedModel):
    file = models.FileField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add files to this product.')
    name = models.CharField(
        max_length=255,
        blank=True)
    description = models.TextField(
        blank=True)
    product = models.ForeignKey(
        Product,
        related_name='files')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Manage Product Files'

    def __unicode__(self):
        return self.file.path

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        extension = extension.replace('.', '')
        return extension.upper()

    @staticmethod
    def move_down(model_type_id, model_id):
        try:
            ModelClass = ContentType.objects.get(id=model_type_id).model_class()
            lower_model = ModelClass.objects.get(id=model_id)
            higher_model = ModelClass.objects.filter(
                product=lower_model.product).filter(
                order__gt=lower_model.order)[0]

            lower_model.order, higher_model.order = higher_model.order, lower_model.order

            higher_model.save()
            lower_model.save()
        except IndexError:
            pass
        except ModelClass.DoesNotExist:
            pass

    @staticmethod
    def move_up(model_type_id, model_id):
        try:
            ModelClass = ContentType.objects.get(id=model_type_id).model_class()

            higher_model = ModelClass.objects.get(id=model_id)
            lower_model = ModelClass.objects.filter(
                product=higher_model.product).filter(
                order__lt=higher_model.order).reverse()[0]

            lower_model.order, higher_model.order = higher_model.order, lower_model.order

            higher_model.save()
            lower_model.save()
        except IndexError:
            pass
        except ModelClass.DoesNotExist:
            pass


class ImageGapWidth(models.Model):
    image = models.ImageField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add images to this gap width.')
    name = models.CharField(
        max_length=255,
        blank=True)
    caption = models.TextField(
        blank=True)
    product_gap_width = models.ForeignKey(
        ProductGapWidth,
        related_name='gap_width_images')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.image.path


class FileGapWidth(ordered_model.OrderedModel):
    file = models.FileField(
        upload_to='catalogue/%Y/%m/%d/',
        help_text='Add files to this gap width.')
    name = models.CharField(
        max_length=255,
        blank=True)
    description = models.TextField(
        blank=True)
    product_gap_width = models.ForeignKey(
        ProductGapWidth,
        related_name='gap_width_files')
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
        auto_now=True)

    class Meta:
        ordering = ('order',)
        verbose_name_plural = 'Manage Gap Width Files'

    def __unicode__(self):
        return self.file.path

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        extension = extension.replace('.', '')
        return extension.upper()

    @staticmethod
    def move_down(model_type_id, model_id):
        try:
            ModelClass = ContentType.objects.get(id=model_type_id).model_class()
            lower_model = ModelClass.objects.get(id=model_id)
            higher_model = ModelClass.objects.filter(
                product=lower_model.product).filter(
                order__gt=lower_model.order)[0]

            lower_model.order, higher_model.order = higher_model.order, lower_model.order

            higher_model.save()
            lower_model.save()
        except IndexError:
            pass
        except ModelClass.DoesNotExist:
            pass

    @staticmethod
    def move_up(model_type_id, model_id):
        try:
            ModelClass = ContentType.objects.get(id=model_type_id).model_class()

            higher_model = ModelClass.objects.get(id=model_id)
            lower_model = ModelClass.objects.filter(
                product=higher_model.product).filter(
                order__lt=higher_model.order).reverse()[0]

            lower_model.order, higher_model.order = higher_model.order, lower_model.order

            higher_model.save()
            lower_model.save()
        except IndexError:
            pass
        except ModelClass.DoesNotExist:
            pass