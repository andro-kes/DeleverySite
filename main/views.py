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
        if form.is_valid():
            value = form.cleaned_data['search_field']
        queryset = OrderModel.objects.filter(category__icontains=value)
        data = {
            'products': queryset,
        }
        return render(request, self.template_results_name, data)