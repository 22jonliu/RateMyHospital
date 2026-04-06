from django.contrib import admin
from .models import Facility, Review, UserProfile

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'zip']
    search_fields = ['name', 'city']
    list_filter = ['state', 'city']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'facility', 'overall_rating', 'annual_salary', 'would_recommend']
    search_fields = ['job_title', 'facility__name']
    list_filter = ['job_title', 'would_recommend']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_title', 'years_of_experience', 'updated_at']
    search_fields = ['user__username', 'work_title']
    list_filter = ['years_of_experience', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']