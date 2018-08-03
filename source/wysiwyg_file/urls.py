
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    # Index
    url(r'^$',
        views.index,
        name='wysiwyg_file-index'),
)
