from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

# About view.
def about(request):
    return render(request, "about.html")

# Booking view.
def booking(request):
    return render(request, "booking.html")

# Doctors view.
def doctors(request):
    return render(request, "doctors.html")

# Contact view.
def contact(request):
    return render(request, "contacts.html")

# Contact view.
def departments(request):
    return render(request, "departments.html")

