from django.urls import path
from . import views

app_name = 'RateMyHospital'

urlpatterns = [
    path('', views.home, name='home'),
    path('hospital/<int:pk>/', views.hospital_detail, name='hospital_detail'),
]