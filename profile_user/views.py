from typing import Any
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from .forms import ProfileUpdateForm
from accounts.models import Cities
from main.models import UserCartModel
from django.urls import reverse_lazy

class ProfileView(UpdateView):
    model = get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'profile_user/profile.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id})

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['cities'] = Cities.objects.all()
        context['cart'] = UserCartModel.objects.filter(user=self.request.user)
        print(UserCartModel.objects.filter(user=self.request.user))
        return context