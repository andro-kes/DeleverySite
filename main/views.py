from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .forms import SearchProductForm
from .models import OrderModel
from django.views.generic.list import ListView

class MainView(View):
    """ 
    Класс для функционала главной страницы
    """
    template_name = 'main/main.html'
    
    # шаблон, на котором будут показываться найденные товары
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
        # находим товары, содержащие данную категорию
        queryset = OrderModel.objects.filter(category__icontains=value)
        # получаем айди всех найденных элементов
        request.session['queryset_ids'] = list(queryset.values_list('id', flat=True))
        return redirect('results')

class ResultsView(ListView):
    """ 
    Класс для показа результатов по поиску продуктов
    """
    template_name = 'main/results.html'
    def get_queryset(self):
        # распаковка чек всех айди через сессию и нахождение их в модели Заказов
        queryset_ids = self.request.session.get('queryset_ids', [])
        return OrderModel.objects.filter(id__in=queryset_ids)

class ProductDetailView(DetailView):
    '''
    Класс для отдельного представления продукта
    '''
    model = OrderModel
    template_name = 'main/detail.html'
    context_object_name = 'product'