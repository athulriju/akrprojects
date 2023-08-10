from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    
class Details(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    email = models.EmailField(max_length=250)
    mobile = models.IntegerField()
    gender = models.CharField(max_length=10,default=True)
    address = models.CharField(max_length=250)
    dob = models.DateField(max_length=250)
    dept = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    material = models.CharField(max_length=250)

    def __str__(self):
        return self.name