from django.db import models
import datetime


# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=200)
    usertype = models.IntegerField(default=0)
class branch(models.Model):
    dateofreg = models.DateField()
    branch_id = models.CharField(max_length=100, default='')
    b_name = models.CharField(max_length=100)
    b_add = models.CharField(max_length=200, default='')
    b_loc = models.CharField(max_length=200)
    b_phone = models.BigIntegerField()
    email=models.CharField(max_length=30, default='')
    password = models.CharField(max_length=200)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class stock(models.Model):
    pname = models.CharField(max_length=100, default='')
    qua = models.IntegerField(default=0)

class product(models.Model):
    categ = models.CharField(max_length=100)

    p_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100,default='nil')
    manfac = models.CharField(max_length=100, default='')
    price = models.CharField(max_length=100, default='')
    stk = models.ForeignKey(stock, on_delete=models.CASCADE, default='')








class Requests(models.Model):
    rdate = models.DateField()
    branch = models.CharField(max_length=100, default='')
    pname = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')



class sample(models.Model):
    idn = models.BigIntegerField
    name = models.CharField(max_length=200)

class employ(models.Model):


    dateofjoin = models.DateField()
    timeofjoin = models.TimeField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender= models.CharField(max_length=100, default='')
    add = models.CharField(max_length=200)
    town = models.CharField(max_length=100, default='')
    district = models.CharField(max_length=100)
    email = models.EmailField()
    phn = models.BigIntegerField()
    out = models.ForeignKey(branch, on_delete= models.CASCADE, default='')







