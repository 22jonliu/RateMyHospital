from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Facility, Review
from django.db.models import Q
import json
from django.http import JsonResponse


def home(request):
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
    hospital = get_object_or_404(Facility, pk=pk)
    reviews = hospital.reviews.all()
    return render(request, 'hospital_detail.html', {
        'hospital': hospital,
        'reviews': reviews
    })


@login_required(login_url='/login/')
def submit_review(request, pk):
    if request.method == 'POST':
        try:
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
                job_title=request.POST.get('job_title', ''),
                department=request.POST.get('department', ''),
                years_of_experience=request.POST.get('years_of_experience', ''),
                pay_type=request.POST.get('pay_type', 'hourly'),
                hourly_rate=clean_numeric(request.POST.get('hourly_rate')),
                annual_salary=clean_numeric(request.POST.get('annual_salary')),
                overall_rating=clean_numeric(request.POST.get('overall_rating')),
                work_life_balance=clean_numeric(request.POST.get('work_life_balance')),
                management=clean_numeric(request.POST.get('management')),
                career_growth=clean_numeric(request.POST.get('career_growth')),
                staffing_levels=clean_numeric(request.POST.get('staffing_levels')),
                pros=request.POST.get('pros', ''),
                cons=request.POST.get('cons', ''),
                would_recommend=request.POST.get('would_recommend') == 'True',
                date_posted=date.today()
            )
            return redirect('RateMyHospital:hospital_detail', pk=pk)
        except Exception as e:
            return redirect('RateMyHospital:hospital_detail', pk=pk)
    return redirect('RateMyHospital:hospital_detail', pk=pk)


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


def account_profile_view(request):
    return render(request, 'account_profile.html')
