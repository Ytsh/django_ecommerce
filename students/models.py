from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    rollNo = models.IntegerField()
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length=100)
    birth_date = models.DateField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    # relation , three types
    #  one to one, one to many/ many to one, many to many