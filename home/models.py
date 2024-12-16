from django.db import models

# Departments.

class Departments(models.Model):
    dep_name = models.CharField(max_length=255)
    dep_description = models.TextField()
    def __str__(self):
        return self.dep_name

# Doctors.
class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')
    def __str__(self):
        return 'Dr ' + self.doc_name + ' - (' + self.doc_spec + ')'

# Booking
class Booking(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=10)
    patient_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

