from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Facility, Review, UserProfile
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('RateMyHospital:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('RateMyHospital:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='main:login')
def profile_view(request):
    """View for user profile page"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()
        
        profile.work_title = request.POST.get('work_title', '')
        profile.years_of_experience = request.POST.get('years_of_experience', 0)
        profile.save()
        
        return redirect('main:profile')
    
    return render(request, 'profile.html', {
        'profile': profile,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    })


def logout_view(request):
    logout(request)
    return redirect('main:home')