# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # Root URL now points directly to the DRF API root
    path('', views.api_root, name='api-root'),

    # Django Admin panel
    path('admin/', admin.site.urls),

    # All other API endpoints
    path('api/', include('core.urls')),

    # Optional: login/logout for browsable API
    path('api-auth/', include('rest_framework.urls')),
]


