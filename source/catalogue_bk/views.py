
import os, tempfile, time, urllib, zipfile
import json

from django.db import transaction
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core.servers.basehttp import FileWrapper

from . import models
from . import ordered_model
from . import forms
from colours.models import Range
from balco_specific.models import PositionApplication, InteriorExterior, CoverType, GapWidth, \
    Movement, ExplainationCopy


def index(request):
    categories = models.Category.objects.all()
    if categories:
        first_category = categories[:1][0]
        return redirect(first_category)

    return render(request, 'catalogue/index.html', locals())


def category_colour_range(request, slug, pk):
    try:
        category = models.Category.objects.get(pk=pk)
    except models.Category.DoesNotExist:
        raise Http404("Category not found with id: {}".format(pk))
    if slug != category.slug:
        raise Http404("Slug in URL does not match category.")

    sub_categories = category.sub_categories.select_related().all()
    colour_ranges = Range.objects.prefetch_related('colours').filter(category=category.pk)
    case_studies = category.case_studies.all()
    selected = request.session.get('selected', False)
    return render(request, 'catalogue/category-colours.html', locals())


def category_detail(request, slug, pk):
    try:
        category = models.Category.objects.select_related().get(pk=pk)
    except models.Category.DoesNotExist:
        raise Http404("Category not found with id: {}".format(pk))
    if slug != category.slug:
        raise Http404("Slug in URL does not match category.")

    images = category.category_images.all()
    sub_categories = category.sub_categories.select_related().all()
    case_studies = category.case_studies.all()
    selected = request.session.get('selected', False)
    return render(request, 'catalogue/category-detail.html', locals())


def product_selector(request, slug, pk):
    try:
        category = models.Category.objects.select_related().get(pk=pk)
    except models.Category.DoesNotExist:
        raise Http404("Category not found with id: {}".format(pk))
    if slug != category.slug:
        raise Http404("Slug in URL does not match category.")

    if pk != '4':
        raise Http404("Only for Balco Expansion & Seismic Joints")

    form = forms.ProductSelectorForm()
    images = category.category_images.all()
    sub_categories = category.sub_categories.select_related().all()
    case_studies = category.case_studies.all()
    selected = request.session.get('selected', False)

    position_applications = PositionApplication.objects.all().order_by('name')
    movement_finders = Movement.objects.all().order_by('name')
    gap_width_finders = GapWidth.objects.all().order_by('name')
    interior_exteriors = InteriorExterior.objects.all().order_by('name')
    cover_types = CoverType.objects.all().order_by('name')

    position_applications_explaination = ExplainationCopy.objects.filter(field=1)
    interior_exteriors_explaination = ExplainationCopy.objects.filter(field=2)
    cover_types_explaination = ExplainationCopy.objects.filter(field=3)
    gap_width_explaination = ExplainationCopy.objects.filter(field=4)
    movement_explaination = ExplainationCopy.objects.filter(field=5)

    # name = ''

    if request.method == "POST":
        is_searched = True
        # name = request.POST.get('name', None)
        position_application = request.POST.get('position_application', None)
        movement_finder = request.POST.get('movement_finder', None)
        gap_width_finder = request.POST.get('gap_width_finder', None)
        interior_exterior = request.POST.get('interior_exterior', None)
        cover_type = request.POST.get('cover_type', None)

        products = models.ProductGapWidth.objects.all()
        if position_application:
            products = products.filter(position_application__id=position_application)
        if movement_finder:
            products = products.filter(movement_finder__id=movement_finder)
        if gap_width_finder:
            products = products.filter(gap_width_finder__id=gap_width_finder)
        if interior_exterior:
            products = products.filter(interior_exterior__id=interior_exterior)
        if cover_type:
            products = products.filter(cover_type__id=cover_type)

    return render(request, 'catalogue/product-selector.html', locals())


def product_codes(request, slug, pk):
    try:
        category = models.Category.objects.select_related().get(pk=pk)
    except models.Category.DoesNotExist:
        raise Http404("Category not found with id: {}".format(pk))
    if slug != category.slug:
        raise Http404("Slug in URL does not match category.")

    code = request.GET.get('query', None)
    products = []
    if code:
        product_gap_widths = models.ProductGapWidth.objects.filter(name__icontains=code, gapwidth_products__sub_category__category=category)
        for product in product_gap_widths:
            products.append({'value': product.name, 'data': product.name})

    return HttpResponse(json.dumps({"suggestions": products}))

def sub_category_detail(request, category_slug, slug, pk, group_slug=None):
    try:
        sub_category = models.SubCategory.objects.select_related().get(pk=pk)
    except models.SubCategory.DoesNotExist:
        raise Http404("Sub Category not found with id: {}".format(pk))
    if slug != sub_category.slug:
        raise Http404("Slug in URL does not match sub category.")

    category = sub_category.category
    if category_slug != category.slug:
        raise Http404("Slug in URL does not match category.")

    case_studies = category.case_studies.all()

    data = dict()
    groups = sub_category.groups.all().order_by('name')
    for group in groups:
        data[group.name] = list()
        data[group.name].append(group)

    products = sub_category.products.all()
    for product in products:
        for group in product.group.all():
            data[group.name].append(product)

    sorted_data = list()
    for k in sorted(data):
        sorted_data.append(data[k])

    sub_categories = category.sub_categories.prefetch_related().all()
    selected = request.session.get('selected', False)
    return render(request, 'catalogue/sub-category-detail.html', locals())


def product_detail(request, slug, pk):

    try:
        product = models.Product.objects.select_related().get(pk=pk)
    except models.Product.DoesNotExist:
        raise Http404("Product not found with id: {}".format(pk))
    if slug != product.slug:
        raise Http404("Slug in URL does not match product.")

    if request.POST:
        response = file_download(request, product)
        if response != False:
            return response

    colour_ranges = product.colour_ranges.all()
    images = product.images.all()
    files = product.files.all()

    sub_category = product.sub_category
    groups = sub_category.groups.all()
    category = sub_category.category

    # Sub navigation extras
    sub_categories = category.sub_categories.all()
    selected = request.session.get('selected', False)
    return render(request, 'catalogue/product-detail.html', locals())

def product_gap_detail(request, slug, pk):

    try:
        product = models.ProductGapWidth.objects.select_related().get(pk=pk)
    except models.Product.DoesNotExist:
        raise Http404("Product not found with id: {}".format(pk))
    if slug != product.slug:
        raise Http404("Slug in URL does not match product.")

    if request.POST:
        response = file_gap_download(request, product)
        if response != False:
            return response

    if product.gapwidth_products.all():
        colour_ranges = product.gapwidth_products.all()[0].colour_ranges.all()
    images = product.gap_width_images.all()
    files = product.gap_width_files.all()

    if product.gapwidth_products.all():
        sub_category = product.gapwidth_products.all()[0].sub_category
        groups = sub_category.groups.all()
        category = sub_category.category

        # Sub navigation extras
        sub_categories = category.sub_categories.all()
    selected = request.session.get('selected', False)
    return render(request, 'catalogue/product-gap-detail.html', locals())

def product_search(request):
    query = request.GET.get('q', '').strip()
    products = models.Product.objects.search(query)

    # Paginate
    products = _pagination(request, products)

    def build_url(page, query):
        return urllib.urlencode(dict(page=page, q=query))

    if products.has_previous():
        page_previous = build_url(products.previous_page_number(), query)
    if products.has_next():
        page_next = build_url(products.next_page_number(), query)

    return render(request, 'catalogue/product-search.html', locals())


def file_download(request, product):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory.
    """

    download_all = request.POST.get('download-all', False)
    if download_all:
        files = product.files.all()
    else:
        keys = request.POST.getlist('download-files')
        if len(keys) < 1:
            return False
        files = models.File.objects.filter(pk__in=keys)

    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for f in files:
        archive.write(f.file.path, os.path.basename(f.file.name))
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')

    filename = time.strftime('{}-%Y-%m-%d.zip'.format(product.slug))
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response

def file_gap_download(request, product):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory.
    """

    download_all = request.POST.get('download-all', False)
    if download_all:
        files = product.gap_width_files.all()
    else:
        keys = request.POST.getlist('download-files')
        if len(keys) < 1:
            return False
        files = models.FileGapWidth.objects.filter(pk__in=keys)

    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for f in files:
        archive.write(f.file.path, os.path.basename(f.file.name))
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')

    filename = time.strftime('{}-%Y-%m-%d.zip'.format(product.slug))
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response

def _pagination(request, products, limit=25):
    paginator = Paginator(products, limit)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        raise Http404('Page not an integer.')
    except EmptyPage:
        raise Http404('Empty page.')
    return products


@staff_member_required
@transaction.commit_on_success
def admin_move_ordered_model(request, direction, model_type_id, model_id):

    ModelClass = ContentType.objects.get(id=model_type_id).model_class()
    if direction == "up":
        ModelClass.move_up(model_type_id, model_id)
    else:
        ModelClass.move_down(model_type_id, model_id)

    url = request.META.get('HTTP_REFERER')
    if url is None:
        app_label = ModelClass._meta.app_label
        model_name = ModelClass.__name__.lower()
        url = "/admin/%s/%s/" % (app_label, model_name)

    return HttpResponseRedirect(url)
