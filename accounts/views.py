from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Signup,Vnr


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=str(password))

        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Username / password is incorrect')
            return redirect('login')
    else:
        return render(request,'login.html')


def signup(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        username=request.POST['username']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        
        if password1==password2:
            x=Vnr.objects.filter(rollnumber=username)
            y=Vnr.objects.filter(email=email)
            
            if Vnr.objects.filter(rollnumber=username).exists()==False:
                messages.info(request,'Invalid Username')
                return redirect('signup')
            elif str(x)!=str(y):
                messages.info(request,'Invalid Email')
                return redirect('signup')
            else:    
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already existing')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already existing')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    sign=Signup.objects.create(full_name=full_name,username=username,email=email,mobile_number=mobile_number,password=password1)
                
                    print('user created')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')