from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages

from accounts.models import Signup
from forms.models import Sellform,Eventform
from .models import Books,Electronics,Stationery,Sports,Others,Favourites

# Create your views here.
def general(sell):
    if sell.category=='Books' or sell.category=='books':
        Books.objects.create(username=sell.username,email=sell.email,product_title=sell.product_title,description=sell.description,price=sell.price,img=sell.img)
    elif sell.category=='Electronics' or sell.category=='electronics':
        Electronics.objects.create(username=sell.username,email=sell.email,product_title=sell.product_title,description=sell.description,price=sell.price,img=sell.img)
    elif sell.category=='Stationery' or sell.category=='stationery':
        Stationery.objects.create(username=sell.username,email=sell.email,product_title=sell.product_title,description=sell.description,price=sell.price,img=sell.img)
    elif sell.category=='Sports' or sell.category=='sports':
        Sports.objects.create(username=sell.username,email=sell.email,product_title=sell.product_title,description=sell.description,price=sell.price,img=sell.img)
    else:
        Others.objects.create(username=sell.username,email=sell.email,product_title=sell.product_title,description=sell.description,price=sell.price,img=sell.img)


def favourite_list(my_username,category):
    f1=Favourites.objects.all()
    l=[]
    fav_seller_username_list=[]
    fav_pt_list=[]
    for f in f1:
        if my_username==f.favourite_username and f.category==category:
            fav_seller_username_list.append(f.username)
            fav_pt_list.append(f.product_title)
    l.append(fav_seller_username_list)
    l.append(fav_pt_list)
    return l


def about(request): 
    return render(request,'about.html')


def books(request,my_username):
    if my_username =='x':
        books1=Books.objects.all()
        return render(request,'books.html',{'books1':books1})
    else:
        books1=Books.objects.all()
        l=favourite_list(my_username,'Books')
        return render(request,'books.html',{'books1':books1,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def electronics(request,my_username):
    if my_username =='x':
        electronics1=Electronics.objects.all()
        return render(request,'electronics.html',{'electronics1':electronics1})
    else:
        electronics1=Electronics.objects.all()
        l=favourite_list(my_username,'Electronics')
        return render(request,'electronics.html',{'electronics1':electronics1,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def event(request):
    event1=Eventform.objects.all()
    return render(request,'event.html',{'event1':event1})


def favourites(request,direct):
    if request.method=='POST':
        pt=request.POST['pt']
        #img=request.FILES['img']
        price=request.POST['price']
        sid=request.POST['sid']
        fid=request.POST['fid']
        cat=request.POST['cat']
        description=request.POST['description']

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
        if Favourites.objects.filter(username=sid,favourite_username=fid,img=img,price=price,product_title=pt,category=cat,description=description).exists():
            f1=Favourites.objects.get(username=sid,favourite_username=fid,img=img,price=price,product_title=pt,category=cat,description=description)
            f1.delete()
        else:
            Favourites.objects.create(username=sid,favourite_username=fid,img=img,price=price,product_title=pt,category=cat,description=description)
        if direct=='favpage':
            return redirect('favourites',direct='favpage')
        elif direct=='single':
            s2=Sellform.objects.get(username=sid,img=img)
            return redirect('single_product_details',my_id=s2.id,my_username=fid)
        else:
            if cat=='Books':
                if direct=='x':
                    return redirect('books',my_username=fid)
                else:
                    b1=Books.objects.get(username=sid,img=img)
                    return redirect('books_product_details',my_id=b1.id,my_username=fid)
            elif cat=='Electronics' :
                if direct=='x':
                    return redirect('electronics',my_username=fid)
                else:
                    e1=Electronics.objects.get(username=sid,img=img)
                    return redirect('electronics_product_details',my_id=e1.id,my_username=fid)
            elif cat=='Sports' :
                if direct=='x':
                    return redirect('sports',my_username=fid)
                else:
                    sp1=Sports.objects.get(username=sid,img=img)
                    return redirect('sports_product_details',my_id=sp1.id,my_username=fid)
            elif cat=='Stationery':
                if direct=='x':
                    return redirect('stationery',my_username=fid)
                else:
                    s1=Stationery.objects.get(username=sid,img=img)
                    return redirect('stationery_product_details',my_id=s1.id,my_username=fid)
            elif cat=='Others':
                if direct=='x':
                    return redirect('others',my_username=fid)
                else:
                    o1=Others.objects.get(username=sid,img=img)
                    return redirect('others_product_details',my_id=o1.id,my_username=fid)
    else:
        f1=Favourites.objects.all()
        favourite_username_list=[]
        for f in f1:
            favourite_username_list.append(f.favourite_username)
        return render(request,'favourites.html',{'f1':f1,'favourite_username_list':favourite_username_list})


def others(request,my_username):
    if my_username =='x':
        others1=Others.objects.all()
        return render(request,'others.html',{'others1':others1})
    else:
        others1=Others.objects.all()
        l=favourite_list(my_username,'Others')
        return render(request,'others.html',{'others1':others1,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})



def books_product_details(request,my_id,my_username):
    if my_username =='x':
        x=Books.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'books_product_details.html',{'x':x,'y':y})
    else:
        x=Books.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,'Books')
        return render(request,'books_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def electronics_product_details(request,my_id,my_username):
    if my_username =='x':
        x=Electronics.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'electronics_product_details.html',{'x':x,'y':y})
    else:
        x=Electronics.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,'Electronics')
        return render(request,'electronics_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def stationery_product_details(request,my_id,my_username):
    if my_username=='x':
        x=Stationery.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'stationery_product_details.html',{'x':x,'y':y})
    else:
        x=Stationery.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,'Stationery')
        return render(request,'stationery_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})

def sports_product_details(request,my_id,my_username):
    if my_username=='x':
        x=Sports.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'sports_product_details.html',{'x':x,'y':y})
    else:
        x=Sports.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,'Sports')
        return render(request,'sports_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})

    
def others_product_details(request,my_id,my_username):
    if my_username=='x':
        x=Others.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        return render(request,'others_product_details.html',{'x':x,'y':y})
    else:
        x=Others.objects.get(id=my_id)
        y=Signup.objects.get(username=x.username)
        l=favourite_list(my_username,'Others')
        return render(request,'others_product_details.html',{'x':x,'y':y,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def favourite_product_details(request,my_id):
    x=Favourites.objects.get(id=my_id)
    y=Signup.objects.get(username=x.username)
    return render(request,'favourite_product_details.html',{'x':x,'y':y})


def sports(request,my_username):
    if my_username =='x':
        sports1=Sports.objects.all()
        return render(request,'sports.html',{'sports1':sports1})
    else:
        sports1=Sports.objects.all()
        l=favourite_list(my_username,'Sports')
        return render(request,'sports.html',{'sports1':sports1,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})


def stationery(request,my_username):
    if my_username =='x':
        stationery1=Stationery.objects.all()
        return render(request,'stationery.html',{'stationery1':stationery1})
    else:
        stationery1=Stationery.objects.all()
        l=favourite_list(my_username,'Stationery')
        return render(request,'stationery.html',{'stationery1':stationery1,'fav_seller_username_list':l[0],'fav_pt_list':l[1]})

