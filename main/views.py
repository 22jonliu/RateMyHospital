from datetime import date

from django.shortcuts import render, get_object_or_404
from matplotlib.pylab import place
from .models import Facility, Review
from django.db.models import Q
import json
from django.http import JsonResponse   


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
@csrf_exempt
def submit_review(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        facility = get_object_or_404(Facility, pk=pk)

        Review.objects.create(
            facility=facility,
            job_title=data['job_title'],
            department=data['department'],
            years_of_experience=data['years_of_experience'],
            pay_type=data['pay_type'],
            hourly_rate=data['hourly_rate'] or 0,
            annual_salary=data['annual_salary'] or None,
            overall_rating=data['overall_rating'],
            work_life_balance=data['work_life_balance'],
            management=data['management'],
            career_growth=data['career_growth'],
            staffing_levels=data['staffing_levels'],
            pros=data['pros'],
            cons=data['cons'],
            would_recommend=data['would_recommend'],
            date_posted=date.today()
        )

        return JsonResponse({'message': 'Review submitted successfully!'}, status=201)

    return JsonResponse({'error': 'POST required'}, status=400)