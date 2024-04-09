from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

class AccountCreationForm(UserCreationForm):
    """ 
    Форма для создания пользователей
    """
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={
                'class': '',
                'placeholder': 'Придумайте пароль', 
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'class': '',
            'placeholder': 'Повторите пароль',
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'address', 'list_warehouse', 
            'list_pick_up_point', 'organization', 
            'production', 'first_name', 'last_name',
        )
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
        
class AccountLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class': '',
        'plcaeholder': 'Введите сюда',
    }))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'class': '',
            'placeholder': 'Введите сюда',
        }),
    )