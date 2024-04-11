from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # регистрация
    path('auth/', include('accounts.urls')),
    
    # главное приложение
    path('', include('main.urls')),
    
    # профиль 
    path('profile/', include('profile_user.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
