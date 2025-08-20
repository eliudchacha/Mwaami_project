from django.apps import AppConfig
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Mwaami Foundation"
    
from django.apps import AppConfig
import os
from django.conf import settings

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # List of subfolders inside MEDIA_ROOT
        folders = [
            'children_photos',
            'blog_image',
            'slides',
            'staff_photos',
            'programs',
            'progress_report',
            'staff_photos',
            'testimonials',
            'advertisements',
            'hero',
            'about',
            'slides',
            'mediacontent',
            'donations',
                  # add others as needed
        ]

        for folder in folders:
            path = os.path.join(settings.MEDIA_ROOT, folder)
            os.makedirs(path, exist_ok=True)
