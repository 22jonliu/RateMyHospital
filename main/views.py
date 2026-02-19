from django.shortcuts import render
from .models import Facility, Review

def home(request):
    """Home page - list all facilities"""
    facilities = Facility.objects.all()
    
    return render(request, 'home.html', {
        'facilities': facilities
    })