import email
from django.shortcuts import render,redirect
from accounts.models import Signupstudent,Signupalumni
from forms.models import Questionform,Answerform,Techansform,Techform
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from passlib.hash import django_pbkdf2_sha256 as handler
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == 'POST':
        username=request.POST['username']
        student_username=request.POST['student_username']
        full_name=request.POST['full_name']
        question=request.POST['question']
        answer=request.POST['answer']
        company=request.POST['company']
        Answerform.objects.create(username=username,student_username=student_username,full_name=full_name,company=company,question=question,answer=answer)
        x=Signupstudent.objects.filter(username=student_username)
        l=x.values('email')
        y=[]
        for each in l:
            y.append(each['email'])
        send_mail(
        'Here is your answer from '+full_name,
        "Your Question : \n"+question+"\n \n \nAnswer: \n"+answer,
        'connect1822@gmail.com',
        y,
        fail_silently=False,
    )
        return redirect('/')
    else:
        sign2=Signupstudent.objects.all()
        sign3=Signupalumni.objects.all()
        qn=Questionform.objects.all()[::-1]
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
        #print('---',sign3,'----')
        return render(request,"index.html",{'sign2':sign2,'sign3':sign3,'qn':qn,'ans':ans,'d':d,'qn1':qn1})

def profile(request):
    sign2=Signupstudent.objects.all()
    sign3=Signupalumni.objects.all()
    return render(request,"profile.html",{'sign2':sign2,'sign3':sign3})
def password(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        password3=request.POST['password3']

        user=auth.authenticate(username=username,password=password1)
        s=Signupstudent.objects.get(username=username)
        u = User.objects.get(username=username)
        if user is None:
            messages.info(request,'Password is incorrect')
            return redirect('password')
        else:
            if password2==password3:
                h = handler.hash(password2)
                u.password=h
                u.save()
                s.password=password2
                s.save()
                return redirect('/')
            else:
                messages.info(request,'passwords doesnt match')
                return redirect('password')
    else:
        return render(request,"password.html")
def password1(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        password3=request.POST['password3']

        user=auth.authenticate(username=username,password=password1)
        s=Signupalumni.objects.get(username=username)
        u = User.objects.get(username=username)
        if user is None:
            messages.info(request,'Password is incorrect')
            return redirect('password1')
        else:
            if password2==password3:
                h = handler.hash(password2)
                u.password=h
                u.save()
                s.password=password2
                s.save()
                return redirect('/')
            else:
                messages.info(request,'passwords doesnt match')
                return redirect('password1')
    else:
        return render(request,"password1.html")

def techform(request):
    if request.method=='POST':
        username=request.POST['username']
        full_name=request.POST['full_name']
        email=request.POST['email']
        question=request.POST['question']
        Techform.objects.create(username=username,full_name=full_name,email=email,question=question)
        li=Signupalumni.objects.all()
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
        return redirect('/')
    else:
        sign = Signupstudent.objects.all()
        return render(request,'techform.html',{'sign':sign})

def technical(request):
    if request.method == 'POST':
        username=request.POST['username']
        student_username=request.POST['student_username']
        full_name=request.POST['full_name']
        question=request.POST['question']
        answer=request.POST['answer']
        Techansform.objects.create(username=username,student_username=student_username,full_name=full_name,question=question,answer=answer)
        x=Signupstudent.objects.filter(username=student_username)
        l=x.values('email')
        y=[]
        for each in l:
            y.append(each['email'])
        send_mail(
            'Here is your answer from '+full_name,
            "Your Question : \n"+question+"\n \n \nAnswer: \n"+answer,
            'connect1822@gmail.com',
            y,
            fail_silently=False,
        )
        return redirect('/technical')
    else:
        sign1=Signupstudent.objects.all()
        sign2=Signupalumni.objects.all()
        ans=Techansform.objects.order_by('question')
        d = {}
        for a in ans:
            current_key = a.question  # the item's date
            d.setdefault(current_key, []).append(a)
        qn=Techform.objects.all()
        ans1=Techansform.objects.all()
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
        return render(request,'technical.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'d':d,'qn1':qn1})
