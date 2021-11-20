from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import Sellform,Eventform,Clubs
from pages.views import general

# Create your views here.
def sellform(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        category=request.POST['category']
        product_title=request.POST['product_title']
        description=request.POST['description']
        price=request.POST['price']
        img=request.FILES['img']
        sell=Sellform.objects.create(username=username,email=email,category=category,product_title=product_title,description=description,price=price,img=img)
        general(sell)
        print('created')
        return redirect('/')
    else:
        return render(request,'sellform.html')
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

        if Clubs.objects.filter(rollnumber=username).exists()==False:
            messages.info(request,'Invalid Username')
            return redirect('eventRegistration')
        else:    
            Eventform.objects.create(username=username,event_name=event_name,start_date=start_date,end_date=end_date,link=link,number=number,description=description,venue=venue,img=img)
            return redirect('/')
    else:
        return render(request,'eventRegistration.html')
