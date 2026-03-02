from datetime import date
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Facility, Review
from django.db.models import Q
import json
from django.http import JsonResponse   
def home(request):
        #Home page with search functionality
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


def reviews(request):
    """View to list hospitals for review"""
    return render(request, 'Review.html')


def facility_list_api(request):
    """API endpoint to return all facilities as JSON"""
    facilities = Facility.objects.all().values('id', 'name', 'city', 'full_address')
    return JsonResponse(list(facilities), safe=False)


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
        try:
            data = json.loads(request.body)
            facility = get_object_or_404(Facility, pk=pk)

            def clean_numeric(val):
                if val == '' or val is None:
                    return None
                try:
                    return float(val)
                except (ValueError, TypeError):
                    return None

            Review.objects.create(
                facility=facility,
                job_title=data.get('job_title', ''),
                department=data.get('department', ''),
                years_of_experience=data.get('years_of_experience', ''),
                pay_type=data.get('pay_type', 'hourly'),
                hourly_rate=clean_numeric(data.get('hourly_rate')),
                annual_salary=clean_numeric(data.get('annual_salary')),
                overall_rating=clean_numeric(data.get('overall_rating')),
                work_life_balance=clean_numeric(data.get('work_life_balance')),
                management=clean_numeric(data.get('management')),
                career_growth=clean_numeric(data.get('career_growth')),
                staffing_levels=clean_numeric(data.get('staffing_levels')),
                pros=data.get('pros', ''),
                cons=data.get('cons', ''),
                would_recommend=data.get('would_recommend') == True or data.get('would_recommend') == 'true',
                date_posted=date.today()
            )

            return JsonResponse({'message': 'Review submitted successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'POST required'}, status=400)
