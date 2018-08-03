
from django import forms

from . import models


# class ProductAdminForm(forms.ModelForm):
#     """
#     Allow for custom validation of product editing in the product admin.
#     """
#     class Meta:
#         model = models.Product


class ProductSelectorForm(forms.ModelForm):

	class Meta:
		model = models.ProductGapWidth
		fields = ('name', 'position_application', 'gap_width_finder', 'movement_finder', 'interior_exterior', 'cover_type',)
