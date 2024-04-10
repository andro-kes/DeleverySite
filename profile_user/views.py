from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from accounts.models import AccountsModel

class ProfileView(DetailView):
    model = AccountsModel
    template_name = 'profile_user/profile.html'
    context_object_name = 'user'