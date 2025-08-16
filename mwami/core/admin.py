from django.contrib import admin
from .models import (
    Child, Sponsor, Donation, Volunteer, BlogPost, ContactMessage, ProgressReport,
    MediaContent, Advertisement, Slide, HeroSection, AboutContent, Program,
    ImpactStat, Testimonial, Staff
)

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sponsored')
    search_fields = ('name', 'bio')
    list_filter = ('sponsored',)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'joined_on')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('joined_on',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'child', 'amount', 'payment_method', 'date_donated')
    search_fields = ('sponsor__full_name', 'child__name', 'amount')
    list_filter = ('payment_method', 'child', 'sponsor')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'skills', 'availability', 'joined_date', 'end_date')
    search_fields = ('full_name', 'email', 'skills')
    list_filter = ('availability', 'joined_date', 'end_date')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_puplished', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('is_puplished', 'created_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_read', 'sent_at')

@admin.register(ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ('child', 'title', 'report_date')
    search_fields = ('child__name', 'title', 'description')
    list_filter = ('report_date',)

@admin.register(MediaContent)
class MediaContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'video', 'uploaded_at')
    search_fields = ('title',)
    list_filter = ('uploaded_at',)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link', 'is_active', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'background_image')

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body', 'image')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')

@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote', 'photo')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'photo')
    search_fields = ('name', 'position')
    list_filter = ('position',)
