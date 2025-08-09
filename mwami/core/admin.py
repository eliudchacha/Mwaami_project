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
    list_display = ('Full_name', 'email', 'phone_number', 'joined_on')
    search_fields = ('Full_name', 'email', 'phone_number')
    list_filter = ('joined_on',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'amount', 'date_donated', 'Child', 'payment_method')
    search_fields = ('sponsor__Full_name', 'Child__name', 'amount')
    list_filter = ('payment_method', 'Child', 'sponsor')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('Full_name', 'email', 'phone_number', 'skills', 'availability')
    search_fields = ('Full_name', 'email')
    list_filter = ('skills', 'joined_date')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)

@admin.register(ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ('Child', 'report_date', 'description')
    search_fields = ('Child__name', 'description')
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
    list_display = ('title', 'image', 'description')
    search_fields = ['title',]


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'background_image')

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote')
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'photo')
    search_fields = ('name', 'position')
    list_filter = ('position',)
