from django.shortcuts import render
from django.views.generic.base import View

class ProfileView(View):
    template_name = 'profile_user/profile.html'
    
    def get(self, request):
        return render(request, self.template_name)