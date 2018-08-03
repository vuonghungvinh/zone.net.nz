
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from . import views


urlpatterns = patterns('',
    # Index
    url(r'^$',
        views.by_product_category,
        name='project_index'),

    # Category detail
    url(r'^entry/(?P<slug>[\w\-]+)/(?P<pk>[\d]+)/$',
        views.category_detail,
        name='project_category_detail'),

    # Grouped by product category
    url(r'product/(?P<product_category_slug>[\w\-]+)/$',
        views.by_product_category,
        name='projects_by_product_category'),

    # Entry detail
    url(r'^entry/(?P<slug>[\w\-]+)/$',
        views.entry_detail,
        name='project_entry_detail'),

    # Related product category / case studies
    url(r'^category/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.product_category_case_studies,
        name='project_category_entries'),

    # Basic Search
    url(r'^search/$',
        views.search,
        name='project_search'),

    # Redactor JSON
    url(r'json/images/(?P<pk>[\d]+)/$',
        views.entry_images_json,
        name='project_images_json'),
)
