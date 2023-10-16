from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CourseRegistration(models.Model):

    PAYMENT_CHOICES = (
        ('bkash', 'Bkash'),
        ('nagad', 'Nagad'),
    )
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    courses = models.CharField(max_length=100)
    bkash_transaction_id = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True,null=True)  # Adjust upload_to to 'images/' based on MEDIA_ROOT
    payment_method = models.CharField(max_length=25, choices=PAYMENT_CHOICES,blank=True,null=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and self.father_name and self.mother_name and self.national_id and self.address and self.mobile_number and self.bkash_transaction_id:
            self.registration_date = timezone.now()
        super().save(*args, **kwargs)
