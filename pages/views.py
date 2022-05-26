import unicodedata
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages

from accounts.models import Signupalumni,Signupstudent
from .models import Analysis
from forms.models import Answerform, Questionform,Eventform,Event,Techansform
from django.db.models import Q
from django.core.mail import send_mail
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt,mpld3
from matplotlib import cm
import seaborn as sns
import re
import unicodedata
import nltk
import string
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import WordNetLemmatizer
import io
import base64
import os,sys
from PIL import Image, ImageTk
nltk.download('wordnet')
nltk.download('omw-1.4')
 
lemmatizer = WordNetLemmatizer()

stopwords = list(STOPWORDS)
s=['knowledge','skills','amazon','work','jpmc','deloitte','tcs','infosys','wipro','accenture','lti','atlassian','ncr','cognizant','capgemini','factset','acs','accolite','f5','statestreet','dbs','major','environment',
'environment','difficulty','level','questions', 'asked','are','required' , 'get', 'placed','youll','you','lot','interviewer','interview']
stopwords.extend(s)



# Create your views here.
def clean_text(text):
    text0=re.sub('<.*?>','',text)
    text1=unicodedata.normalize('NFKD',text0).encode('ascii','ignore').decode('utf-8','ignore')
    text2=re.sub(r'https\S+','',text1)
    text3=re.sub('\s+',' ',text2)
    text4=re.sub(r'\b\d+\b','',text3)
    text5=re.sub(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$','',text4)
    text6="".join([c for c in text5 if c not in string.punctuation])
    tokens=re.split(r'\W+',text6)
    text7=[word for word in tokens if word not in stopwords]
    text=" ".join([lemmatizer.lemmatize(word) for word in text7])
    return text

def about(request): 
    return render(request,'about.html')

def discussions(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.all()[::-1]
    techans=Techansform.objects.all()[::-1]
    return render(request,'discussions.html',{'sign1':sign1,'sign2':sign2,'ans':ans,'techans':techans})

def amazon(request):
    if request.method=='POST':
        question=request.POST['question']
        answer=request.POST['answer']
        companyname=request.POST['companyname']
        usernameans= request.POST['usernameans']
        Analysis.objects.create(question=question,answer=answer,companyname=companyname,usernameans=usernameans)
        return redirect('amazon')
    else:
        sign1=Signupstudent.objects.all()
        sign2=Signupalumni.objects.all()
        ans=Answerform.objects.filter(company='Amazon').order_by('question')
        d = {}
        qnanalysis= ['What are the major skills required to get placed in Amazon ?','How is the work environment in Amazon ?','What is the difficulty level of coding questions asked in Amazon ?']
        ansanalysis=Analysis.objects.filter(companyname='Amazon')

        for a in ans:
            current_key = a.question  # the item's date
            d.setdefault(current_key, []).append(a)
        qn=Questionform.objects.filter(companyname1='Amazon')[::-1]
        ans1=Answerform.objects.all()
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

        analysis=[]
        for x in qnanalysis:
            flag=0
            for y in ansanalysis:
                if x == y.question and y.usernameans == current_user.username:
                    flag=1
                    break
            if flag==0:
                analysis.append(x)
        #question 1
        an=Analysis.objects.filter(question=qnanalysis[0])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud.png')
        #question 2
        an=Analysis.objects.filter(question=qnanalysis[1])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud1.png')
        #question 3
        an=Analysis.objects.filter(question=qnanalysis[2])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud2.png')
        return render(request,'amazon.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'d':d,'qn1':qn1,'analysis':analysis})

def jpmc(request):
    if request.method=='POST':
        question=request.POST['question']
        answer=request.POST['answer']
        companyname=request.POST['companyname']
        usernameans= request.POST['usernameans']
        Analysis.objects.create(question=question,answer=answer,companyname=companyname,usernameans=usernameans)
        return redirect('jpmc')
    else:
        sign1=Signupstudent.objects.all()
        sign2=Signupalumni.objects.all()
        ans=Answerform.objects.filter(company='JPMC').order_by('question')
        d = {}
        qnanalysis= ['What are the major skills required to get placed in JPMC ?','How is the work environment in JPMC ?','What is the difficulty level of coding questions asked in JPMC ?']
        ansanalysis=Analysis.objects.filter(companyname='JPMC')

        for a in ans:
            current_key = a.question  # the item's date
            d.setdefault(current_key, []).append(a)
        qn=Questionform.objects.filter(companyname1='JPMC')[::-1]
        ans1=Answerform.objects.all()
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

        analysis=[]
        for x in qnanalysis:
            flag=0
            for y in ansanalysis:
                if x == y.question and y.usernameans == current_user.username:
                    flag=1
                    break
            if flag==0:
                analysis.append(x)
        #question 1
        an=Analysis.objects.filter(question=qnanalysis[0])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud3.png')
        #question 2
        an=Analysis.objects.filter(question=qnanalysis[1])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud4.png')
        #question 3
        an=Analysis.objects.filter(question=qnanalysis[2])
        v=[]
        for each in an:
            v.append(each.answer)
        df = pd.DataFrame(v)
        df.columns=['Answer']
        df['clean_answer']=df['Answer'].apply(lambda x: clean_text(x.lower()))
        df1=df[['clean_answer']]
        plt.figure(figsize=(20,30))
        print(df1)
        os.chdir(r'C:\Users\Dell\major\Student-alumni\static\img')
        s=""
        for i in range(len(df1)) :
            value = df1.loc[i, "clean_answer"]
            # Create and generate a word cloud image:
            #mask2 = np.array(Image.open("circle.png"))
            s=s+" "+ value
        wordcloud = WordCloud(background_color="white", stopwords=stopwords,height=400,width=400)
        wordcloud.generate(s)
        wordcloud.to_file('wordcloud5.png')
        return render(request,'jpmc.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'d':d,'qn1':qn1,'analysis':analysis})
def deloitte(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Deloitte').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Deloitte')
    ans1=Answerform.objects.all()
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
    return render(request,'deloitte.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def tcs(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='TCS').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='TCS')
    ans1=Answerform.objects.all()
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
    return render(request,'tcs.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def infosys(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Infosys').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Infosys')
    ans1=Answerform.objects.all()
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
    return render(request,'infosys.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def wipro(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Wipro').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Wipro')
    ans1=Answerform.objects.all()
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
    return render(request,'wipro.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def accenture(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Accenture').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Accenture')
    ans1=Answerform.objects.all()
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
    return render(request,'accenture.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def lti(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='LTI').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='LTI')
    ans1=Answerform.objects.all()
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
    return render(request,'lti.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def atlassian(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Atlassian').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Atlassian')
    ans1=Answerform.objects.all()
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
    return render(request,'atlassian.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def ncr(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='NCR').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='NCR')
    ans1=Answerform.objects.all()
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
    return render(request,'ncr.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def cognizant(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Cognizant').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Cognizant')
    ans1=Answerform.objects.all()
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
    return render(request,'cognizant.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def factset(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Facset').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Facset')
    ans1=Answerform.objects.all()
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
    return render(request,'factset.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def capgemini(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Capgemini').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Capgemini')
    ans1=Answerform.objects.all()
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
    return render(request,'capgemini.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def acs(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='ACS').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='ACS')
    ans1=Answerform.objects.all()
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
    return render(request,'acs.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def accolite(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Accolite').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Accolite')
    ans1=Answerform.objects.all()
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
    return render(request,'accolite.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def f5(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='F5').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='F5')
    ans1=Answerform.objects.all()
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
    return render(request,'f5.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def statestreet(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='Statestreet').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='Statestreet')
    ans1=Answerform.objects.all()
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
    return render(request,'statestreet.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def dbs(request):
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    ans=Answerform.objects.filter(company='DBS').order_by('question')
    d = {}
    for a in ans:
        current_key = a.question  # the item's date
        d.setdefault(current_key, []).append(a)
    qn=Questionform.objects.filter(companyname1='DBS')
    ans1=Answerform.objects.all()
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
    return render(request,'dbs.html',{'ans':ans,'sign1':sign1,'sign2':sign2,'qn':qn,'d':d,'qn1':qn1})

def others(request):
    companies=['Amazon','JPMC','Deloitte','TCS','Infosys','Wipro','Accenture','LTI','Atlassian','NCR','Cognizant','Factset','Capgemini','ACS','Accolite','F5','Statestreet','DBS']
    sign1=Signupstudent.objects.all()
    sign2=Signupalumni.objects.all()
    qn=Questionform.objects.filter(companyname1='Others')
    ans= Answerform.objects.exclude(company__in=companies)
    ans1=Answerform.objects.all()
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
    return render(request,'others.html',{'sign1':sign1,'sign2':sign2,'qn':qn,'ans':ans,'qn1':qn1})

def event(request):
    event1=Eventform.objects.all()
    event=Event.objects.all()
    return render(request,'event.html',{'event1':event1,'event':event})

def statistics(request):
    return render(request,'statistics.html')

