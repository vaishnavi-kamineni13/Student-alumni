from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Vnr,Signupalumni,Signupstudent
from forms.models import Questionform,Answerform


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=str(password))

        if user is not None:
            auth.login(request,user)
            sign2=Signupstudent.objects.all()
            sign3=Signupalumni.objects.all()
            qn=Questionform.objects.all()
            ans = Answerform.objects.all().order_by('question')
            ans1=Answerform.objects.all()
            d = {}
            for a in ans:
                current_key = a.question  # the item's date
                d.setdefault(current_key, []).append(a)
            qn1=[]
            current_user = request.user
            for q in qn:
                flag=0
                for a in ans1:
                    if q.question == a.question and a.username == current_user.username:
                        flag=1
                        break
                if flag==0:
                    qn1.append(q)
            return render(request,'index.html',{'sign2':sign2,'sign3':sign3,'qn':qn,'qn1':qn1,'ans':ans,'d':d})
        else:
            messages.info(request,'Username / password is incorrect')
            return redirect('login')
    else:
        return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')    

def signupstudent(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        username=request.POST['username']
        branch = request.POST['branch']
        gender = request.POST['gender']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        
        if password1==password2:
            x=Vnr.objects.filter(rollnumber=username)
            y=Vnr.objects.filter(email=email)
            x1=str(username)
            y1=x1[:2]
            if Vnr.objects.filter(rollnumber=username).exists()==False:
                messages.info(request,'Invalid Username')
                return redirect('signupstudent')
            elif y1!='18' and y1!='19' and y1!='20' and y1!='21':
                messages.info(request,'Invalid Student Username')
                return redirect('signupstudent')
            elif str(x)!=str(y):
                messages.info(request,'Invalid Email')
                return redirect('signupstudent')
            else:    
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already existing')
                    return redirect('signupstudent')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already existing')
                    return redirect('signupstudent')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    sign=Signupstudent.objects.create(full_name=full_name,username=username,branch=branch,gender=gender,email=email,mobile_number=mobile_number,password=password1)       
                    print('user created')

        else:
            messages.info(request,'password not matching')
            return redirect('signupstudent')
        return redirect('/')
    else:
        return render(request,'signupstudent.html')

def signupalumni(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        username=request.POST['username']
        branch = request.POST['branch']
        gender = request.POST['gender']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']
        working=request.POST['working']
        company_name=request.POST['company_name']
        dateofjoining = request.POST['dateofjoining']
        designation=request.POST['designation']
        worklocation=request.POST['worklocation']
        company_name1=request.POST['company_name1']
        company_name2=request.POST['company_name2']
        company_name3=request.POST['company_name3']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            x=Vnr.objects.filter(rollnumber=username)
            y=Vnr.objects.filter(email=email)
            x1=str(username)
            y1=x1[:2]            
            if Vnr.objects.filter(rollnumber=username).exists()==False:
                messages.info(request,'Invalid Username')
                return redirect('signupalumni')
            elif y1=='18' or y1=='19' or y1=='20' or y1=='21on ':
                messages.info(request,'Invalid Alumni Username')
                return redirect('signupalumni')
            elif str(x)!=str(y):
                messages.info(request,'Invalid Email')
                return redirect('signupalumni')
            else:    
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already existing')
                    return redirect('signupalumni')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already existing')
                    return redirect('signupalumni')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    sign=Signupalumni.objects.create(full_name=full_name,username=username,branch=branch,gender=gender,email=email,mobile_number=mobile_number,working=working,company_name=company_name,dateofjoining=dateofjoining,designation=designation,worklocation=worklocation,company_name1=company_name1,company_name2=company_name2,company_name3=company_name3,password=password1)
                
                    print('user created')
        else:
            messages.info(request,'password not matching')
            return redirect('signupalumni')
        return redirect('/')
    else:
        return render(request,'signupalumni.html') 
def logout(request):
    auth.logout(request)
    return redirect('/')