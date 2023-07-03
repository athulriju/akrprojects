from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password= password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password, first_name= firstname, last_name= lastname, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password doesnt match')
            return redirect('register')

        
    return render(request,'registration.html')

def logout (request):
    auth.logout(request)
    return redirect('/')