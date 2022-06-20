from django import forms
from buyer.models import *


class CategotyForm(forms.Form):
    db = Category.objects.all()
    category = forms.CharField(label='Category', max_length=100, widget=forms.TextInput(
        {'class': "form-control validate"}))
    categories = forms.ChoiceField(choices=[(x.name, x.name) for x in db], widget=forms.Select(
        {'class': "form-control validate"}))
