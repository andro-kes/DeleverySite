from django import forms

class SearchProductForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(attrs={
        'class': '',
        'placeholder': '',
    }))