from django.forms import Form
from django import forms

class SearchProductForm(Form):
    seacrh_field = forms.TextInput(attrs={
        'class': '',
        'placeholder': '',
    })