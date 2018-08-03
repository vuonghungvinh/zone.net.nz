
from django.contrib import admin
from django.db import models
from django import forms

from models import PositionApplication, InteriorExterior, CoverType, GapWidth, Movement, ExplainationCopy

admin.site.register(PositionApplication)
admin.site.register(InteriorExterior)
admin.site.register(CoverType)
admin.site.register(GapWidth)
admin.site.register(Movement)
admin.site.register(ExplainationCopy)
