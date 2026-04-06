from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.reviews, name='reviews'),
    path('api/facilities/', views.facility_list_api, name='facility_list_api'),
    path('hospital/<int:pk>/', views.hospital_detail, name='hospital_detail'),
    path('hospital/<int:pk>/review/', views.submit_review, name='submit_review'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]