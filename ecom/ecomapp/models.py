from typing import Any
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Catagory(models.Model):
   name=models.CharField(max_length=50,null=False,blank=False)
   description=models.CharField(max_length=250,null=False,blank=False)
   img=models.ImageField( upload_to='./static/pimg')
   status=models.BooleanField(default=False)
   createdtime=models.DateTimeField( auto_now_add=True)

   def __str__(self):
      return self.name

class Products(models.Model):
   cname=models.ForeignKey(Catagory,on_delete=models.CASCADE)
   name=models.CharField(null=False,max_length=50,blank=False)
   description=models.CharField(null=False,max_length=250,blank=False)
   img=models.ImageField( upload_to='./static/pimg')
   status=models.BooleanField(default=False)
   trending=models.BooleanField(default=False)
   supplier=models.CharField(null=False,max_length=50,blank=False)
   createdtime=models.DateTimeField( auto_now_add=True)
   qty=models.IntegerField(null=False,blank=False)
   sp=models.FloatField(null=False,blank=False)
   op=models.FloatField(null=False,blank=False)

   def __str__(self):
      return self.name
   
class Car(models.Model):
   product=models.ForeignKey(Products,on_delete=models.CASCADE)
   user=models.IntegerField(null=False,blank=False)
   proq=models.IntegerField(null=False,blank=False)
   time=models.DateTimeField( auto_now_add=True)

   
  






   

   

   

   
   
