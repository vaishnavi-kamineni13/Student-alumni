from django.shortcuts import render,redirect
from accounts.models import Signup
from .models import Request,Orders
from pages.models import Books,Electronics,Stationery,Sports,Others,Favourites
from forms.models import Sellform
from pages.views import favourite_list
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from passlib.hash import django_pbkdf2_sha256 as handler
# Create your views here.
def index(request):
    sell=Sellform.objects.all()[::-1][:10]
    return render(request,"index.html",{'sell':sell})
def profile(request):
    sign1=Signup.objects.all()
    return render(request,"profile.html",{'sign1':sign1})
def password(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        password3=request.POST['password3']

        user=auth.authenticate(username=username,password=password1)
        s=Signup.objects.get(username=username)
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
def single_product_details(request,my_id,my_username):
    if my_username =='x':
        x=Sellform.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'single_product_details.html',{'x':x,'y':y})
    else:
        x=Sellform.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,x.category)
        return render(request,'single_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})
"""def x():
    x=Sellform.objects.get(id=my_id)
    y=x.username
    u=username
    Request.objects.create_user(y=y,u,pproduct_title)"""
def requests(request,my_id,bool):
    if request.method=='POST':
        pt=request.POST['pt']
        uid=request.POST['uid']
        #img=request.FILES['img']
        price=request.POST['price']
        sid=request.POST['sid']
        cat=request.POST['cat']

        if cat=='Books':
            b1=Books.objects.get(product_title=pt,price=price)
            img=b1.img
        elif cat=='Electronics':
            e1=Electronics.objects.get(product_title=pt,price=price)
            img=e1.img
        elif cat=='Stationery':
            s1=Stationery.objects.get(product_title=pt,price=price)
            img=s1.img
        elif cat=='Sports':
            sp1=Sports.objects.get(product_title=pt,price=price)
            img=sp1.img
        else:
            o1=Others.objects.get(product_title=pt,price=price)
            img=o1.img
        if uid==sid:
            messages.info(request,'You Are The Seller !!')
            return redirect('requests',bool='x',my_id=1)
        else:
            if Request.objects.filter(seller_username=sid,buyer_username=uid,img=img,price=price,product_title=pt,category=cat).exists():
                messages.info(request,'Request already sent')
            else:
                Request.objects.create(seller_username=sid,buyer_username=uid,product_title=pt,img=img,price=price,category=cat)
            return redirect('requests',bool='x',my_id=1)
    else:
        if bool=='Accept':
            r2=Request.objects.get(id=my_id)
            Orders.objects.create(seller_username=r2.seller_username,buyer_username=r2.buyer_username,img=r2.img,price=r2.price,product_title=r2.product_title,category=r2.category)
            s2=Sellform.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
            if r2.category=='Books':
                b1=Books.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
                b1.delete()
            elif r2.category=='Electronics':
                e1=Electronics.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
                e1.delete()
            elif r2.category=='Stationery':
                s1=Stationery.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
                s1.delete()
            elif r2.category=='Sports':
                sp1=Sports.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
                sp1.delete()
            else:
                o1=Others.objects.get(username=r2.seller_username,img=r2.img,product_title=r2.product_title,price=r2.price)
                o1.delete()
            f1=Favourites.objects.all()
            for f in f1:
                if f.username ==r2.seller_username and f.product_title== r2.product_title:
                    f.delete()
            s2.delete()
            r2.delete()
            r1=Request.objects.all()
            request_seller_list=[]
            request_buyer_list=[]
            for r in r1:
                request_seller_list.append(r.seller_username)
                request_buyer_list.append(r.buyer_username)
            return render(request,"requests.html",{'r1':r1,'request_seller_list':request_seller_list,'request_buyer_list':request_buyer_list})
        elif bool=='Decline':
            r2=Request.objects.get(id=my_id)
            r2.delete()
            r1=Request.objects.all()
            request_seller_list=[]
            request_buyer_list=[]
            for r in r1:
                request_seller_list.append(r.seller_username)
                request_buyer_list.append(r.buyer_username)
            return render(request,"requests.html",{'r1':r1,'request_seller_list':request_seller_list,'request_buyer_list':request_buyer_list})
        else:
            r1=Request.objects.all()
            request_seller_list=[]
            request_buyer_list=[]
            for r in r1:
                request_seller_list.append(r.seller_username)
                request_buyer_list.append(r.buyer_username)
            return render(request,"requests.html",{'r1':r1,'request_seller_list':request_seller_list,'request_buyer_list':request_buyer_list})
def orders(request):
    o1=Orders.objects.all()
    return render(request,"orders.html",{'o1':o1})
def sold(request):
    o1=Orders.objects.all()
    return render(request,"sold.html",{'o1':o1})

