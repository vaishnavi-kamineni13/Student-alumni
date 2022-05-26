import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import Questionform,Eventform
from accounts.models import Signupstudent,Signupalumni
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
def general(companyname1,question):
    li=Signupalumni.objects.filter(Q(company_name=companyname1)|Q(company_name1=companyname1)|Q(company_name2=companyname1)|Q(company_name3=companyname1))
    l=li.values('email')
    x=[]
    for each in l:
        x.append(each['email'])
    send_mail(
        'You have a question from Connect!',
        question+"\n \n \n \nPlease login to answer",
        'connect1822@gmail.com',
        x,
        fail_silently=False,
    )
def questionform(request):
    if request.method=='POST':
        username=request.POST['username']
        full_name=request.POST['full_name']
        email=request.POST['email']
        companyname1=request.POST['companyname1']
        companyname2=request.POST['companyname2']
        question=request.POST['question']
        Questionform.objects.create(username=username,full_name=full_name,email=email,companyname1=companyname1,companyname2=companyname2,question=question)
        general(companyname1,question)
        return redirect('/')
    else:
        sign = Signupstudent.objects.all()
        return render(request,'questionform.html',{'sign':sign})

def eventRegistration(request):
    if request.method=='POST':
        username=request.POST['username']
        event_name=request.POST['event_name']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        link=request.POST['link']
        number=request.POST['number']
        description=request.POST['description']
        venue=request.POST['venue']
        img=request.FILES['img']
        Eventform.objects.create(username=username,event_name=event_name,start_date=start_date,end_date=end_date,link=link,number=number,description=description,venue=venue,img=img)
        return redirect('events')
    else:
        return render(request,'eventregistration.html')
