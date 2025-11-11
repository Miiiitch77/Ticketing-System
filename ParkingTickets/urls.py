from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.car_registration, name='car_registration'),
    path('checkout/<int:record_id>/', views.checkout, name='checkout'),
    path('exit/', views.exit_parking, name='exit_parking'),
    path('contact/', views.contact_help, name='contact_help'),
]
