"""
URL configuration for Bazar Akademicki - Student Marketplace with Django Oscar.
"""
from django.apps import apps
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    
    # Homepage
    path('', HomePageView.as_view(), name='home'),
    
    # Oscar URLs
    path('', include(apps.get_app_config('oscar').urls[0])),
    
    # Oscar API
    path('api/', include('oscarapi.urls')),
    
    # Custom user profile URLs
    path('profile/', include('users.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
