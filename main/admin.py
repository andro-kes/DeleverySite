from django.contrib import admin
from .models import OrderModel, UserCartModel

admin.site.register(OrderModel)
admin.site.register(UserCartModel)