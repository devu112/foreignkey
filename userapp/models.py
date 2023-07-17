from django.db import models


# Create your models here.

class course(models.Model):
    coursename =models.CharField(max_length=255)
    fee = models.IntegerField()


class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    studentname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    joiningdate=models.DateField()  

