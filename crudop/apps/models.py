from django.db import models

# Create your models here.
class passmodel(models.Model):
    aadhar = models.BigIntegerField(primary_key= True)
    pname = models.CharField(max_length=50 ,null=False)
    email = models.EmailField(max_length=70, null=False)
    gender = models.CharField(max_length=11, null= False)
    contact = models.CharField(max_length=12,null=False,)
    pin = models.IntegerField(null=False)
    dob= models.DateField(null=False)