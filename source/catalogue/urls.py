
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    # Index
    url(r'^$',
        views.index,
        name='catalogue-index'),

    # Category Colour Range
    url(r'^category/colors/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.category_colour_range,
        name='catalogue-category-colours'),

    # Category detail
    url(r'^category/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.category_detail,
        name='catalogue-category-detail'),

    # Sub Category detail
    url(r'^category/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.sub_category_detail,
        name='catalogue-sub-category-detail'),

    # Product Group Anchor
    url(r'^category/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/(?P<group_slug>[-\w]+)/$',
        views.sub_category_detail,
        name='catalogue-group'),

    # Product detail
    url(r'^product/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.product_detail,
        name='catalogue-product-detail'),

    # Product Search
    url(r'^search/$',
        views.product_search,
        name='catalogue-product-search'),

    # Product gap width detail
    url(r'^product-gap/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.product_gap_detail,
        name='catalogue-product-gap-detail'),

    # Product Selector detail
    url(r'^product-selector/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.product_selector,
        name='product-selector'),

    # Product code search
    url(r'^codes/(?P<slug>[-\w]+)/(?P<pk>[\d]+)/$',
        views.product_codes,
        name='product-codes'),
)
