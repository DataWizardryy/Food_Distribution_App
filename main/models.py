from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    food_description = models.TextField()
    quantity = models.CharField(max_length=50)
    available_until = models.DateField()
    location = models.CharField(max_length=100)  # Format: "latitude,longitude"

    def __str__(self):
        return f"{self.food_description} - {self.donor.name}"


class Request(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    requester_name = models.CharField(max_length=100)
    requester_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"Request by {self.requester_name} for {self.food_item}"


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    area_of_service = models.CharField(max_length=100)

    def __str__(self):
        return self.name

