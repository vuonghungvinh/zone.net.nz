import os
from django.db import models
from django.utils import timezone

from catalogue.models import Category as ProductCategory


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50,
        verbose_name='URL Fragment',
        help_text='Suggested value generated from name.')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse(
            'project-category-detail',
            kwargs={'slug': self.slug, 'pk': self.pk})

    def __unicode__(self):
        return self.name


class EntryManager(models.Manager):

    use_for_related_fields = True

    def get_published(self):
        """
        Entries with status of `live` and `published` date in the past.
        """
        return self.get_live().filter(published__lte=timezone.now())

    def get_live(self):
        """
        Entries with a `status` of live.
        """
        return self.get_query_set().filter(status=self.model.LIVE)


class Entry(models.Model):
    """
    Project

    By default only LIVE entries published in the past will be visible.
    """
    # Status constants
    LIVE = 1
    DRAFT = 2
    STATUS_CHOICES = (
        (LIVE, 'Live'),
        (DRAFT, 'Draft'),
    )

    # Fields
    category = models.ForeignKey(Category, related_name='entries')
    title = models.CharField(max_length=255)
    slug = models.SlugField(help_text=('Used to generate URL. '
            'Suggested value generated from title.'),
            unique=True,
            verbose_name='URL Fragment')
    cover_image = models.ImageField(upload_to='projects/image/%Y/%m/%d/',
        help_text='Add a cover image to this entry.')
    image_caption = models.TextField(blank=True)
    published = models.DateTimeField(
        default=timezone.now,
        help_text=("If publication date and time is in the future the "
            "entry will not be visible until then."))
    file = models.FileField(
        upload_to='projects/file/%Y/%m/%d/',
        help_text='Add a case study to this entry.',
        verbose_name='Case Study')

    # Options
    featured = models.BooleanField(default=False)
    product_categories = models.ManyToManyField(ProductCategory, related_name='case_studies')
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=LIVE,
        help_text="Only Live entries are publicly visible.")

    # Body
    excerpt = models.TextField(
        blank=True,
        help_text="Optionally override the automatically derived exerpt")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = EntryManager()

    class Meta:
        ordering = ['-published']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project_entry_detail', (self.slug,), {})

    def file_extension(self):
        name, extension = os.path.splitext(self.file.name)
        extension = extension.replace('.', '')
        return extension.upper()


class Image(models.Model):
    image = models.ImageField(upload_to='projects/image/%Y/%m/%d/',
        help_text='Add images to this entry.')
    caption = models.TextField(blank=True)
    entry = models.ForeignKey(Entry, related_name='images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.image.path
