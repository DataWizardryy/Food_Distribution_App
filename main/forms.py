from django import forms
from .models import Donor, FoodItem, Request, Volunteer

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
