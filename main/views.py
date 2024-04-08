from django.shortcuts import render
from django.views.generic.base import View

class MainView(View):
    template_name = 'main/main.html'
    
    def get(self, request):
        return render(request, self.template_name)
