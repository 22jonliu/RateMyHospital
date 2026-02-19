from django.contrib import admin
from .models import Facility, Review

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