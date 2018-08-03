
from django.contrib import admin
from django.db import models
from django import forms

from models import Category, CategoryImage, Group, File, Image, Product, SubCategory, ProductGapWidth, \
    ImageGapWidth, FileGapWidth, CategoryFile
from widgets import RedactorTextarea


class ImageAdmin(admin.TabularInline):
    extra = 1
    model = Image
    verbose_name_plural = 'Images'


class FileAdmin(admin.TabularInline):
    extra = 1
    model = File
    verbose_name_plural = 'Files'


class ImageGapWidthAdmin(admin.TabularInline):
    extra = 1
    model = ImageGapWidth
    verbose_name = 'Image'
    verbose_name_plural = 'Images'


class FileGapWidthAdmin(admin.TabularInline):
    extra = 1
    model = FileGapWidth
    verbose_name = 'File'
    verbose_name_plural = 'Files'


class ProductForm(forms.ModelForm):
    """
    This form is specifically for providing Entry instance inforation for the
    redactor settings. In this case the PK
    """
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Get Entry Object Instance
        instance = kwargs.get('instance')

        if instance:
            self.fields['group'].queryset = Group.objects.filter(sub_category=instance.sub_category)
        else:
            self.fields['group'].queryset = Group.objects.none()

        # JSON Redactor settings
        settings = '{'
        settings += '"minHeight": "350"'
        settings += '}'

        self.fields['description'].widget = RedactorTextarea(attrs={'data-settings': settings})
        self.fields['excerpt'].widget = RedactorTextarea(attrs={'data-settings': settings})

    class Meta:
        model = Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    filter_horizontal = ('group', 'related_products', 'colour_ranges', 'projects', 'gapwidth',)
    inlines = (ImageAdmin, FileAdmin,)
    list_display = ('name', 'sub_category', 'order_link', 'format_groups', 'featured', 'created', 'updated')
    list_display_links = ('name',)
    list_filter = ('sub_category', 'group',)
    list_per_page = 50
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description',)

    fieldsets = (
        ('Manage related Products, Projects & Colours', {
            'classes': ('collapse',),
            'fields': ('related_products', 'colour_ranges', 'projects', ),
        }),
        ('Add Gap Width Variations to Balco products', {
            'classes': ('collapse',),
            'fields': ('gapwidth',),
        }),
        (None, {
            'fields': ('featured', 'sub_category', 'group', 'name', 'sub_title', 'slug', 'page_name', 'meta_description', 'cover_image', 'excerpt', 'description',),
        }),
    )

    def format_groups(self, product):
        return ', '.join(g.name for g in product.group.all() )
    format_groups.short_description = 'Groups'
    format_groups.admin_order_field = 'group'


class CategoryImageAdmin(admin.TabularInline):
    extra = 1
    model = CategoryImage
    verbose_name_plural = 'Images'


class CategoryFileAdmin(admin.TabularInline):
    extra = 1
    model = CategoryFile
    verbose_name_plural = 'Files'


class CategoryForm(forms.ModelForm):
    """
    This form is specifically for providing Entry instance inforation for the
    redactor settings. In this case the PK
    """
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        # Get Entry Object Instance
        instance = kwargs.get('instance')

        # JSON Redactor settings
        settings = '{'
        settings += '"minHeight": "200"'
        settings += '}'

        self.fields['description'].widget = RedactorTextarea(attrs={'data-settings': settings})

    class Meta:
        model = Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    filter_horizontal = ('colour_ranges',)
    list_display = ('name', 'order_link', 'created', 'updated')
    inlines = (CategoryImageAdmin, CategoryFileAdmin,)
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description',)
    form = CategoryForm


class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_link_files', 'product',)
    list_display_links = ('name',)
    list_filter = ('product',)
    ordering = ('product', 'order')


class GroupAdminInline(admin.TabularInline):
    extra = 1
    model = Group
    prepopulated_fields = {'slug': ('name',)}


class GroupAdmin(admin.ModelAdmin):
    model = Group
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'sub_category', 'order_link')
    list_filter = ('sub_category',)


class SubCategoryForm(forms.ModelForm):
    """
    This form is specifically for providing Entry instance inforation for the
    redactor settings. In this case the PK
    """
    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)

        # Get Entry Object Instance
        instance = kwargs.get('instance')

        # JSON Redactor settings
        settings = '{'
        settings += '"minHeight": "200"'
        settings += '}'

        self.fields['description'].widget = RedactorTextarea(attrs={'data-settings': settings})

    class Meta:
        model = SubCategory


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order_link', 'created', 'updated')
    list_filter = ('category',)
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description',)
    inlines = (GroupAdminInline,)
    form = SubCategoryForm


class ProductGapWidthAdmin(admin.ModelAdmin):
    list_display = ('name', 'gap_width', 'movement', 'created', 'updated')
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description',)
    inlines = (ImageGapWidthAdmin, FileGapWidthAdmin,)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'cover_image', 'excerpt', 'description', 'gap_width', 'movement',),
        }),
        ('Manage Product Finder', {
            'classes': ('collapse',),
            'fields': ('position_application', 'interior_exterior', 'cover_type', 'gap_width_finder', 'movement_finder'),
        }),
    )

    settings = '{"minHeight": "200"}' # JSON string
    formfield_overrides = {
        models.TextField: {'widget': RedactorTextarea(attrs={'data-settings': settings})},
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(ProductGapWidth, ProductGapWidthAdmin)