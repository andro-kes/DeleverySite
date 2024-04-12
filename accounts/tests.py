from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Cities

class CitiesModelTest(TestCase):
    def setUp(self):
        Cities.objects.create(name='City 1')
        Cities.objects.create(name='City 2')

    def test_city_name(self):
        city = Cities.objects.get(name='City 1')
        self.assertEqual(str(city), 'City 1')

    def test_city_count(self):
        self.assertEqual(Cities.objects.count(), 2)

class AccountsModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        city1 = Cities.objects.create(name='City 1')
        city2 = Cities.objects.create(name='City 2')
        self.user.address.add(city1, city2)
        self.user.list_warehouse.add(city1)
        self.user.list_pick_up_point.add(city2)
        self.user.organization = 'Test Organization'
        self.user.production = 'Test Production'
        self.user.save()

    def test_user_address(self):
        self.assertEqual(self.user.address.count(), 2)

    def test_user_list_warehouse(self):
        self.assertEqual(self.user.list_warehouse.count(), 1)

    def test_user_list_pick_up_point(self):
        self.assertEqual(self.user.list_pick_up_point.count(), 1)

    def test_user_organization(self):
        self.assertEqual(self.user.organization, 'Test Organization')

    def test_user_production(self):
        self.assertEqual(self.user.production, 'Test Production')

    def test_user_str(self):
        self.assertEqual(str(self.user.username), 'testuser')
        
        
from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import AccountCreationForm
from .models import Cities

class AccountCreationFormTest(TestCase):
    def setUp(self):
        self.city1 = Cities.objects.create(name='City 1')
        self.city2 = Cities.objects.create(name='City 2')

    def test_form_valid(self):
        data = {
            'username': 'testuser',
            'address': [self.city1.id],
            'list_warehouse': [self.city1.id],
            'list_pick_up_point': [self.city2.id],
            'password1': 'testpass12345',
            'password2': 'testpass12345', 
            'organization': 'Test Organization',
            'production': 'Test Production',
            'first_name': 'Test',
            'last_name': 'User',
            'status': 'test status'
        }
        form = AccountCreationForm(data)
        print(form.errors)

        self.assertTrue(form.is_valid())


    def test_form_invalid(self):
        data = {
            'username': '',
            'address': ['Каракен'],
            'list_warehouse': ['Каракен'],
            'list_pick_up_point': ['Каракен'],
            'password1': 'фывtestpass12345',
            'password2': 'фывtestpass12345',
            'organization': 'Test Organization',
            'production': 'Test Production',
            'first_name': 'Test',
            'last_name': 'User',
        }
        form = AccountCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('address', form.errors)
        self.assertIn('list_warehouse', form.errors)
        self.assertIn('list_pick_up_point', form.errors)

    def test_form_save(self):
        data = {
            'username': 'testuser',
            'address': [self.city1.id, self.city2.id],
            'list_warehouse': [self.city1.id],
            'list_pick_up_point': [self.city2.id],
            'password1': 'фывtestpass12345',
            'password2': 'фывtestpass12345',
            'organization': 'Test Organization',
            'production': 'Test Production',
            'first_name': 'Test',
            'last_name': 'User',
            'status': 'status',
        }
        form = AccountCreationForm(data)
        user = form.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.address.count(), 2)
        self.assertEqual(user.list_warehouse.count(), 1)
        self.assertEqual(user.list_pick_up_point.count(), 1)
        self.assertEqual(user.organization, 'Test Organization')
        self.assertEqual(user.production, 'Test Production')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertTrue(user.check_password('фывtestpass12345'))
