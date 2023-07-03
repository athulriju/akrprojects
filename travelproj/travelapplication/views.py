from django.shortcuts import render
from travelapplication.models import Persons, Place
from django.contrib.auth.models import User


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2=Persons.objects.all()
    user=User.objects.all()
    return render(request,'index.html',{'result':obj,'persons':obj2,'user':user})