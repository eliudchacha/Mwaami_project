from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import (
    ChildViewSet,
    SponsorViewSet,
    DonationViewSet,
    MediaContentViewSet,
    SlideViewSet,
    AdvertisementViewSet,
    HeroSectionViewSet,
    AboutContentViewset,
    ProgramViewSet,
    ImpactStatViewSet,
    TestimonialViewSet,
    StaffViewSet
)

router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='children')
router.register(r'sponsors', SponsorViewSet, basename='sponsors')
router.register(r'donation', DonationViewSet, basename='donation')
router.register(r'media', MediaContentViewSet, basename='media')
router.register(r'slides', SlideViewSet, basename='slides')
router.register(r'ads', AdvertisementViewSet, basename='ads')
router.register(r'hero', HeroSectionViewSet, basename='hero')
router.register(r'about', AboutContentViewset, basename='about')
router.register(r'programs', ProgramViewSet, basename='programs')
router.register(r'impactstats', ImpactStatViewSet, basename='impact')
router.register(r'testimonials', TestimonialViewSet, basename='testimonials')
router.register(r'staff', StaffViewSet, basename = 'staff')
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.api_root),

]
