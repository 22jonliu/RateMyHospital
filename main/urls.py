from django.urls import path
from django.contrib import admin
from . import views


app_name = 'RateMyHospital'

urlpatterns = [
    path('', views.home, name='home'),
    path('hospital/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('hospital/<int:pk>/submit/', views.submit_review, name='submit_review'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]