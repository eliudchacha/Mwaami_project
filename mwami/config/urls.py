# config/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views
from . import settings
urlpatterns = [
    # Root URL now points directly to the DRF API root
    path('', views.api_root, name='api-root'),

    # Django Admin panel
    path('admin/', admin.site.urls),

    # All other API endpoints
    path('api/', include('core.urls')),

    # Optional: login/logout for browsable API

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


