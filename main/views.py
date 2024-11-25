from django.shortcuts import render

# Create views here.

from django.shortcuts import render, redirect
from .models import Donor, FoodItem, Request, Volunteer
from .forms import DonorForm, FoodItemForm, RequestForm, VolunteerForm

# Home
def home(request):
    return render(request, 'main/home.html')

# Register Donor
def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonorForm()
    return render(request, 'main/register_donor.html', {'form': form})

# Add Food
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodItemForm()
    return render(request, 'main/add_food.html', {'form': form})

# Food Availability Map
def food_map(request):
    food_items = FoodItem.objects.all()
    return render(request, 'main/food_map.html', {'food_items': food_items})

# Request Food
def request_food(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RequestForm()
    return render(request, 'main/request_food.html', {'form': form})

# Volunteer Coordination
def volunteer_coordination(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VolunteerForm()
    return render(request, 'main/volunteer_coordination.html', {'form': form})

