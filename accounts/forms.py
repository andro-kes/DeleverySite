from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'address', 'list_warehouse', 
            'list_pick_up_point', 'password1', 'password2', 
            'organization', 'production', 'first_name', 'last_name',
        )
    # address = models.ManyToManyField(Cities, related_name='address', null=True, blank=True)
    # list_warehouse = models.ManyToManyField(Cities, related_name='list_warehouse', null=True, blank=True)
    # list_pick_up_point = models.ManyToManyField(Cities, related_name='list_pick_up_point', null=True, blank=True)
    # organization = models.CharField(max_length=50, null=True, blank=True)
    # production = models.CharField(max_length=50, null=True, blank=True)
        widgets = {
            'address': forms.CheckboxSelectMultiple(
                attrs = {
                    'class': '',
                    'placeholder': '',
                }
            ),
             'list_warehouse': forms.CheckboxSelectMultiple(
                attrs = {
                    'class': '',
                    'placeholder': '',
                }
            ),
              'list_pick_up_point': forms.CheckboxSelectMultiple(
                attrs = {
                    'class': '',
                    'placeholder': '',
                }
            ),
              'organization': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': ''
                }
            ),
            'production': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': ''
                }
            )
        }