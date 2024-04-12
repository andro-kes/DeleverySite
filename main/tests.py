from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import OrderModel
from accounts.models import Cities

class OrderModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # создаем тестового пользователя
        user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        # создаем тестовый город
        city = Cities.objects.create(name='Test City')
        # создаем тестовый товар
        order = OrderModel.objects.create(
            name='Test Product',
            price=100,
            size='S',
            mass=1.0,
            description='Test product description',
            company=user,
            category='test_category',
        )
        order.warehouse.add(city)
        order.save()

    def test_order_model(self):
        order = OrderModel.objects.get(id=1)
        # проверяем, что поля имеют правильные значения
        self.assertEqual(order.name, 'Test Product')
        self.assertEqual(order.price, 100)
        self.assertEqual(order.size, 'S')
        self.assertEqual(order.mass, 1.0)
        self.assertEqual(order.description, 'Test product description')
        self.assertEqual(order.category, 'test_category')
        self.assertEqual(str(order), 'Test Product')
        self.assertTrue(isinstance(order.warehouse.all()[0], Cities))
        self.assertEqual(order.warehouse.all()[0].name, 'Test City')

    def test_order_str(self):
        order = OrderModel.objects.get(id=1)
        # проверяем, что метод __str__ возвращает правильное значение
        self.assertEqual(str(order), 'Test Product')