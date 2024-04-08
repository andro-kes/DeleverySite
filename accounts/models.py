from django.db import models
from django.contrib.auth.models import AbstractUser

class Cities(models.Model):
    '''
    Модель для всех доступных городов
    '''
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class AccountsModel(AbstractUser):
    """
    Модель с доп полями для аккаунта. Одна для пользователя и компании
    """
    address = models.ManyToManyField(Cities, related_name='address', blank=True)
    list_warehouse = models.ManyToManyField(Cities, related_name='list_warehouse', blank=True)
    list_pick_up_point = models.ManyToManyField(Cities, related_name='list_pick_up_point', blank=True)
    organization = models.CharField(max_length=50, null=True, blank=True)
    production = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.username)