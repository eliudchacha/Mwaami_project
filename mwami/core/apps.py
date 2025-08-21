from django.apps import AppConfig
import os
from django.conf import settings


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Mwaami Foundation"

    def ready(self):
        """
        Ensure required media subfolders exist inside MEDIA_ROOT.
        Safe for local + Render (if MEDIA_ROOT is on a persistent disk).
        """
        folders = [
            'children_photos',
            'blog_image',
            'slides',
            'staff_photos',
            'programs',
            'progress_report',
            'testimonials',
            'advertisements',
            'hero',
            'about',
            'mediacontent',
            'donations',
        ]

        media_root = getattr(settings, "MEDIA_ROOT", None)
        if media_root and os.access(os.path.dirname(media_root), os.W_OK):
            for folder in folders:
                os.makedirs(os.path.join(media_root, folder), exist_ok=True)
