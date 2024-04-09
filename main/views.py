from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect 
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .forms import SearchProductForm
from .models import OrderModel, UserCartModel
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

class MainView(View):
    """ 
    Класс для функционала главной страницы
    """
    template_name = 'main/main.html'
    
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
    
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    if product_id:
        product = OrderModel.objects.get(id=product_id)
        user_cart = UserCartModel.objects.get(user=request.user)
        user_cart.products.add(product)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})

class ProductDetailView(DetailView):
    '''
    Класс для отдельного представления продукта
    '''
    model = OrderModel
    template_name = 'main/detail.html'
    context_object_name = 'product'