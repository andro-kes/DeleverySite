from django import forms
from django.contrib.auth import get_user_model

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'address',
            'list_warehouse', 'organization',
            'list_pick_up_point', 'production',
        )

        widgets = {
            'address': forms.CheckboxSelectMultiple(),

            'list_warehouse': forms.CheckboxSelectMultiple(),

            'list_pick_up_point': forms.CheckboxSelectMultiple(),

            'organization': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': 'Введите сюда'
                }
            ),
            'production': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': 'Введите сюда'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': 'Ваше имя'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': 'Ваша фамилия'
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': '',
                    'placeholder': 'E-mail'
                }
            ),
        }
