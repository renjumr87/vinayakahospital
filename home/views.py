from django.shortcuts import render
from django.http import HttpResponse
from . models import Departments, Doctors
from . forms import BookingForm
# Index view
def index(request):
    return render(request, "index.html")

# About view.
def about(request):
    return render(request, "about.html")

# Booking view.
def booking(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, "booking.html", dict_form)

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

