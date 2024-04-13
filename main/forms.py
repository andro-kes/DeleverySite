from django import forms
from .models import OrderModel

class SearchProductForm(forms.Form):
    """ 
    Поисковая форма для товаров
    """
    search_field = forms.CharField(widget=forms.TextInput(attrs={
        'class': '',
        'placeholder': 'Поиск',
    }))
    
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        
        widgets = {
            'picture1': forms.FileInput(attrs={
                'data-imgid': "pic1",
                'accept': 'media/'
            }),
            'picture2': forms.FileInput(attrs={
                'data-imgid': "pic2",
            }),
            'picture3': forms.FileInput(attrs={
                'data-imgid': "pic3",
            }),
            'name': forms.TextInput(attrs={'placeholder': 'Название товара'}),
            'mass': forms.NumberInput(attrs={'placeholder': 'Масса'}),
            'size': forms.TextInput(attrs={'placeholder': 'Размер'}),
            'category': forms.TextInput(attrs={'placeholder': 'Теги'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Цена'}),
            'category': forms.TextInput(attrs={'hidden': True}),
            'list_warehouse': forms.CheckboxSelectMultiple(),
            'status': forms.TextInput(attrs={'hidden': True}),
            'description': forms.TextInput(attrs={'placeholder': 'Описание'}),
        }
        
class ChangeStatusForm(forms.Form):
    number = forms.CharField()
    status = forms.CharField()
    
class OrderProductForm(forms.Form):
    status = forms.CharField(widget=forms.TextInput(attrs={'id': 'order_status'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'id': 'order_price'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'id': 'order_number'}))
    delevery = forms.CharField(widget=forms.TextInput(attrs={'id': 'order_delevery'}))