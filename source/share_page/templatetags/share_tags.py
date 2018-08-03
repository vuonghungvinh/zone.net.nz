"""
Template tags for the share page application.
"""

from django import template
from django.contrib import messages
from django.shortcuts import redirect

from share_page import forms
from share_page import views

register = template.Library()


@register.inclusion_tag('share_page/form.html')
def share_form(request):
    if request.method == 'POST':
        form = forms.ShareForm(request.POST, path=request.path)
    else:
        form = forms.ShareForm(path=request.path)
    return {'form': form}

