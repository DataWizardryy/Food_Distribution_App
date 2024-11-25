from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-donor/', views.register_donor, name='register_donor'),
    path('add-food/', views.add_food, name='add_food'),
    path('food-map/', views.food_map, name='food_map'),
    path('request-food/', views.request_food, name='request_food'),
    path('volunteer-coordination/', views.volunteer_coordination, name='volunteer_coordination'),
]
