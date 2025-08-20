from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import api_views

# DRF router
router = routers.DefaultRouter()
router.register(r'children', api_views.ChildViewSet, basename='child')
router.register(r'sponsors', api_views.SponsorViewSet, basename='sponsor')
router.register(r'volunteers', api_views.VolunteerViewSet, basename='volunteer')
router.register(r'blogposts', api_views.BlogPostViewSet, basename='blogpost')
router.register(r'slides', api_views.SlideViewSet, basename='slide')
router.register(r'mediacontent', api_views.MediaContentViewSet, basename='mediacontent')
router.register(r'advertisements', api_views.AdvertisementViewSet, basename='advertisement')
router.register(r'heropages', api_views.HeroSectionViewSet, basename='herosection')
router.register(r'programs', api_views.ProgramViewSet, basename='program')
router.register(r'impactstats', api_views.ImpactStatViewSet, basename='impactstat')
router.register(r'about', api_views.AboutContentViewSet, basename='aboutcontent')
router.register(r'staff', api_views.StaffViewSet, basename='staff')
router.register(r'testimonials', api_views.TestimonialViewSet, basename='testimonial')
router.register(r'donations', api_views.DonationViewSet, basename='donations')
router.register(r'message', api_views.ContactMessageViewSet, basename='contactmessage')
router.register(r'progressreports', api_views.ProgressReportViewSet, basename='progressreport')  # <-- added

urlpatterns = [
    path('api/', include(router.urls)),               # DRF API root
    path('api-auth/', include('rest_framework.urls')) # Login/Logout tab
]
