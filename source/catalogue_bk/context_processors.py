"""
A set of request processors that return dictionaries to be merged into a
template context.
"""

from django.conf import settings

from .models import Category

def categories(request):
    """
    Adds metadata-related context variables to the context.
    """
    categories = Category.objects.prefetch_related('sub_categories').all()
    categories = list(categories)   # Force run of query
    return {
        'categories': categories,
    }
