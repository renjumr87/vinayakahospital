from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments, Doctors

# Index view
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
    dict_docs = {
        
        'doct': Doctors.objects.all()
    }
    return render(request, "doctors.html", dict_docs)

# Contact view.
def contact(request):
    return render(request, "contact.html")

# Departments view.
def departments(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request, "departments.html", dict_dept)

