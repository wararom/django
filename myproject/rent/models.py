from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car (models.Model):
    # image = models.ImageField(upload_to='cars')
    model = models.CharField(max_length=20)
    detail = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
      return self.model

class Rent (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateTimeField()
    stop = models.DateTimeField(null=True)
    fee = models.DecimalField(max_digits=10,decimal_places=2,null=True)


# Create your models here.
'''
First Name
Last Name
Telephone
Date of Birth
Credit Amount
Profile Image
Memo 500 characters
'''
class Person(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	telephone=models.CharField(max_length=15,null=True)
	dob=models.DateField(blank=True,null=True)
	credit_amount=models.DecimalField(max_digits=15, decimal_places=2)
	memo=models.CharField(max_length=500,null=True)

