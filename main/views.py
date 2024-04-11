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
from openpyxl import load_workbook
import heapq
import os

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
    """
    Добавление в корзину
    """
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
    
    @classmethod
    def dijkstra(self, graph, start):
        distances = {city: float('infinity') for city in graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_city = heapq.heappop(pq)

            if current_distance > distances[current_city]:
                continue

            for neighbor in graph[current_city]:
                distance = current_distance + neighbor['distance']

                if distance < distances[neighbor['city']]:
                    distances[neighbor['city']] = distance
                    heapq.heappush(pq, (distance, neighbor['city']))

        return distances
    
    @classmethod
    def to_graph(self):
        # Открываем Excel файл
        app_path = os.path.dirname(__file__)

        # Построение пути к файлу по земле
        file_path_earth = os.path.join(app_path, 'Расстояния.xlsx')
        # По воздуху
        file_path_air = os.path.join(app_path, 'Расстояния_воздух.xlsx')
        # Выбираем активный листы
        wb = load_workbook(file_path_earth)
        sheet = wb.active
        
        wb_air = load_workbook(file_path_air)
        sheet_air = wb_air.active
        # Преобразуем данные в виде графа
        cities_index_list = []
        for city in sheet.iter_rows(min_row=1, max_row=1, values_only=True):
            for name in city:
                if name:
                    cities_index_list.append(name)
        data_list = []
        for city in sheet.iter_rows(min_row=2, values_only=True):
            data = [{'city': city[0]}]
            for i in range(1, len(city)):
                if city[i] != None:
                    if city[i] != '-':
                        data.append({'city': cities_index_list[i-1], 'distance': int(city[i])})
            data_list.append(data)
            
        data_list_air = []
        for city in sheet_air.iter_rows(min_row=2, values_only=True):
            data = [{'city': city[0]}]
            for i in range(1, len(city)):
                if city[i] != None:
                    if city[i] != '-':
                        data.append({'city': cities_index_list[i-1], 'distance': int(city[i])})
            data_list_air.append(data)
        # Преобразуем данные в виде графа
        graph = {}
        for city_data in data_list:
            city = city_data[0]['city']
            graph[city] = [{'city': data['city'], 'distance': data['distance']} for data in city_data[1:]]
        
        graph_air = {}
        for city_data in data_list:
            city = city_data[0]['city']
            graph_air[city] = [{'city': data['city'], 'distance': data['distance']} for data in city_data[1:]]
        return (graph, graph_air)
    
    def get_context_data(self, **kwargs: Any):
        # Скорость доставки в км/ч
        v = 50
        v_air = 200
        # Цена за каждый час в рублях
        price_list = 100
        price_list_air = 500
        
        context =  super().get_context_data(**kwargs)  
        # Получим город пользователя
        address = self.request.user.address.all()[0].name
        # Получим склады товара
        list_warehouse = []
        for warehouse in self.object.warehouse.all():
            list_warehouse.append(warehouse.name)
        # Получим пункты выдачи компании
        company = self.object.company
        list_pick_up_point = []
        for pick_up_point in company.list_pick_up_point.all():
            list_pick_up_point.append(pick_up_point.name)
        # Получим все расстояния
        shortest_paths = self.dijkstra(self.to_graph()[0], address)
        shortest_paths_air = self.dijkstra(self.to_graph()[1], address)
        # Найдем расстояния до каждого склада
        list_distance = []
        list_distance_air = []
        for warehouse in list_warehouse:
            distance = shortest_paths[warehouse]
            list_distance.append(distance)
        for warehouse in list_warehouse:
            distance = shortest_paths_air[warehouse]
            list_distance_air.append(distance)
        
        if address in list_pick_up_point:
            context['econom'] = min(list_distance)/v
            context['fast'] = min(list_distance_air)/v_air
            context['result_price_fast'] = (min(list_distance_air)/v)*price_list_air + int(self.object.price)
            context['result_price_econom'] = (min(list_distance)/v)*price_list + int(self.object.price)
        else:
            context['econom'] = (min(list_distance)/v)
            context['result_price'] = (min(list_distance)/v)*2*price_list + int(self.object.price)
            context['fast'] = (min(list_distance_air)/v_air)
            context['result_price_fast'] = (min(list_distance_air)/v)*2*price_list_air + int(self.object.price)
            context['notifiction'] = 'В вашем городе нет нашего пункта выдачи, поэтому доставка дороже :('
        return context