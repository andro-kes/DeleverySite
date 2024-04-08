from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # регистрация
    path('auth/', include('accounts.urls')),
    
    # главное приложение
    path('', include('main.urls')),
]
