from django.shortcuts import render, get_object_or_404
from .models import Facility, Review
from django.db.models import Q

def home(request):
    """Home page with search functionality"""
    query = request.GET.get('q')
    facilities = None
    if query:
        facilities = Facility.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query)
        )
    
    return render(request, 'home.html', {
        'facilities': facilities,
        'query': query
    })

def hospital_detail(request, pk):
    """Show details and reviews for a specific hospital"""
    hospital = get_object_or_404(Facility, pk=pk)
    reviews = hospital.reviews.all()
    
    return render(request, 'hospital_detail.html', {
        'hospital': hospital,
        'reviews': reviews
    })
