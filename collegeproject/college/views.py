

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Department, Course, Details
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def next(request):
    return render(request,'next.html')
def enquiry(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        mobile=request.POST['mobile']
        email=request.POST['email']
        gender=request.POST['gender']
        address=request.POST['address']
        dept=request.POST['dept']
        course=request.POST['course']
        purpose=request.POST['purpose']
        selected_materials = request.POST.getlist('material')
        selected_materials_str = ', '.join(selected_materials)
        print(selected_materials_str)
        form=Details.objects.create(name=name,age=age,email=email,mobile=mobile,gender=gender,address=address,dob=dob,dept=dept,course=course,purpose=purpose,material=selected_materials_str)
        form.save()
        messages.info(request,"Order Confirmed")
    obj=Department.objects.all()
    from datetime import datetime

    today = datetime.now().date().strftime('%Y-%m-%d')

    return render(request,'enquiry.html', {'today': today,'obj': obj})



from django.http import JsonResponse

def get_courses(request):
    id = request.GET.get('id') 
    courses = Course.objects.filter(dept=id).values('name','dept')
    return JsonResponse(list(courses), safe=False)



def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        
        email="sample@gmail.com"
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Usename Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"Email Taken")
            #     return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name="null",last_name="null",email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not match")  
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'next.html')
        else:
            messages.info(request,"invalid input")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
