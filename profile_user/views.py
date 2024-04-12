from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from .forms import ProfileUpdateForm
from accounts.models import Cities
from main.models import UserCartModel
from django.urls import reverse_lazy
from main.forms import SearchProductForm

class ProfileUpdateView(UpdateView):
    model = get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'profile_user/profile_update.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('profile_update', kwargs={'pk': self.request.user.id})

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['cities'] = Cities.objects.all()
        context['cart'] = UserCartModel.objects.get(user=self.request.user).products.all()
        context['form_search'] = SearchProductForm()
        return context
    
class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile_user/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['cities'] = Cities.objects.all()
        
        profile_user_id = self.object.id
        profile_user = self.model.objects.get(id=profile_user_id)
        context['address'] = profile_user.address.all()
        context['warehouses'] = profile_user.list_warehouse.all()
        context['pick_up_points'] = profile_user.list_pick_up_point.all()
        context['form_search'] = SearchProductForm()
        return context