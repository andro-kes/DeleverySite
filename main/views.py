from django.shortcuts import render
from django.views.generic.base import View
from .forms import SearchProductForm
from .models import OrderModel

class MainView(View):
    template_name = 'main/main.html'
    template_results_name = 'main/results.html'
    
    def get(self, request):
        data = {
            'form': SearchProductForm(),
        }
        return render(request, self.template_name, data)
    def post(self, request, *args, **kwargs):
        form = SearchProductForm(request.POST)
        value = form.seacrh_field
        if value:
            queryset = OrderModel.objects.filter(category__icontains=value)
        else:
            queryset = ''
        data = {
            'products': queryset,
        }
        return render(request, self.template_results_name, data)