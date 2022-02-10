from django.db import models

# Create your models here.
class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    intakename=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()

