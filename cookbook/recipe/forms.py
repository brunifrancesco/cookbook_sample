from django import forms
from django.core.exceptions import ValidationError


class NewRecipeForm(forms.Form):
   name = forms.CharField(label="Name")
   ingredients = forms.CharField(label="Ingredients", widget=forms.Textarea)
   method = forms.CharField(label="Method")

   def clean_name(self):
      if (len(self.cleaned_data['name']) > 10):
         raise ValidationError("Invalid value", code='invalid')
      return self.cleaned_data['name'].upper()
