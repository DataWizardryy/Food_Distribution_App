from django.contrib import admin
from .models import Donor, FoodItem, Request, Volunteer

# Register models here

admin.site.register(Donor)
admin.site.register(FoodItem)
admin.site.register(Request)
admin.site.register(Volunteer)
