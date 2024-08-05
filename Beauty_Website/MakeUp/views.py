from django.db.models import Q
from django.shortcuts import render,redirect
from MakeUp.models import Category,Product,Main_category
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def sale(request):
    return render(request,'sale.html')
def allcategories(request,n):
    m= Main_category.objects.get(name= n)
    c=Category.objects.filter(categories=m)
    p = Product.objects.filter(category__in=c)
    return render(request,'category.html',{'c':c,'p':p,'m':m})
def allproducts(request,p):
    c = Category.objects.get(name= p)
    m= c.categories
    r= Category.objects.filter(categories=m)
    p = Product.objects.filter(category =c)
    return render(request,'product.html',{'c':c,'p':p,'r':r})
def detail(request,p):
    p = Product.objects.get(name=p)
    return render(request,'details.html',{'p':p})

def register(request):
    if (request.method == "POST"):
        n = request.POST['n']
        p = request.POST['p']
        cp = request.POST['cp']
        nl = request.POST['nl']
        e = request.POST['e']

        if (p == cp):
            user = User.objects.create_user(username=n, password=p, last_name=nl, email=e)
            user.save()
            return redirect('MakeUp:userlogin')
        else:
            return HttpResponse("password same")

    return render(request, 'register.html')


def userlogin(request):
    if (request.method == 'POST'):
        n = request.POST['n']
        p = request.POST['p']
        user = authenticate(username=n,password=p)
        if user:
            login(request,user)
            return redirect('MakeUp:home')
        else:
            return HttpResponse("invalid response")
    return render(request,'login.html')


def userlogout(request):
    logout(request)
    return redirect('MakeUp:userlogin')

def search(request):
    b= None
    q=""
    if(request.method == "POST"):
        q=request.POST['q']
        if q:
            b=Product.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})



