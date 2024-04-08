from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View
from .forms import AccountCreationForm

class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

class AccountLogoutView(LogoutView):
    pass

class SignUpView(View):
    template_name = 'accounts/signup.html'
    
    def get(self, request):
        form = AccountCreationForm()
        data = {
            'form': form
        }
        return render(request, self.template_name, data)
    
    def post(self, request, *args, **kwargs):
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        data = {
            'form': form,
        }
        return render(request, self.template_name, data)