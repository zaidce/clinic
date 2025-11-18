from django.db import models
from datetime import datetime
# Create your models here.
class Client (models.Model):
      bloodChoices={
        ("لا اعرف","لا اعرف"),
        ("A+","A+"),
        ("B+","B+"),
        ("AB+","AB+"),
        ("O+","O+"),
          ("A-","A-"),
        ("B-","B-"),
        ("AB-","AB-"),
        ("O-","O-"),
        }
      mariageChoices={
        ("اعزب","اعزب"),
        ("متزوج","متزوج"),
        ("مطلق","مطلق"),
        ("ارمل","ارمل")
        }
      name=models.CharField(max_length=200)
      bornYear=models.IntegerField(default=0)
      phone=models.CharField(max_length=11)
      address=models.CharField(max_length=200,null=True,blank=True)
      gender=models.BooleanField(default=False)
      alergy=models.CharField(max_length=200,null=True,blank=True)
      desiase=models.CharField(max_length=200,null=True,blank=True)
      blood=models.CharField(max_length=20,choices=bloodChoices,default="لا اعرف")
      mariage=models.CharField(max_length=20,choices=mariageChoices,default="اعزب")
      lastOperations=models.CharField(max_length=200,null=True,blank=True)
      smooker=models.BooleanField(default=False)
      hidden=models.BooleanField(default=False)
      note=models.CharField(max_length=200,null=True,blank=True)
      def __str__(self):
        return self.name