
import os, tempfile, time, urllib, zipfile
import json

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core.servers.basehttp import FileWrapper
from django.views.decorators.csrf import csrf_exempt

from . import models

@csrf_exempt
def index(request):
    image = models.Image()
    image.image = request.FILES['file']
    image.save()

    return HttpResponse(json.dumps({
    	'url': image.image.url,
    	'filelink': image.image.url,
    	'id': image.id
	}), content_type="application/json")