from django import forms

class SearchProductForm(forms.Form):
    """ 
    Поисковая форма для товаров
    """
    search_field = forms.CharField(widget=forms.TextInput(attrs={
        'class': '',
        'placeholder': '',
    }))