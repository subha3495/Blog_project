from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=50)
    esalary=models.IntegerField()
    eage=models.IntegerField()