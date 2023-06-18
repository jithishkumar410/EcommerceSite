from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.db.models import Q

# Create your views here.
 
def home(request):
    catag=Catagory.objects.all()
    pro=Products.objects.filter(trending=True)
    return render(request,'home.html',{"catg":catag,'pro':pro})

def reg(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'reg.html', { 'f': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            
            return redirect('log')
        else:
            return render(request, 'reg.html', {'f': form})
def log(request):       
    if request.method == 'GET':
            form = LoginForm()
            return render(request, 'log.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome!')
                return redirect('home')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'log.html',{'form': form})
    
    
def Logout(request):
    
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('log')

def cart(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,"Please register or login")
       
        return render(request,'cart.html')
    elif Car.objects.filter(user=request.user.id,product=id):
        messages.warning(request,"You already add this item in cart")
        return redirect('allcart')

    else:
       
        
        
        pro=Products.objects.filter(id=id)
        r=Car.objects.create(user=request.user.id,product=pro[0],proq=2)
        r.save()
        rt=Car.objects.filter(user=request.user.id)
        t=0
        for i in rt:
            t=t+i.product.op
        
       
        return render(request,'cart.html',{'pro':rt,'t':t})
    
def delcart(request,id):
    n=Car.objects.filter(user=request.user.id,product_id=id)
    n.delete()
    return redirect('allcart')


def allcart(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please register or login")
    else:
        rt=Car.objects.filter(user=request.user.id)
        t=0
        for i in rt:
            t=t+i.product.op
        
        return render(request,'cart.html',{'pro':rt,'t':t})

        
    
def cat(request):
    catag=Catagory.objects.all()
    return render(request,'cata.html',{'catg':catag})





def pro(request,name):
    if Catagory.objects.filter(id=name):
        pro=Products.objects.filter(cname_id=name)
        return render(request,'product.html',{'pro':pro})
    else:
        messages.warning(request,"NOT Found")
        return redirect('home')
  
def pd(request,id):
    
    if Products.objects.filter(id=id):
        print(request.GET)
        if request.method == 'GET':
            qty = request.POST.get('qty')
            print(qty)
        pro=Products.objects.filter(id=id)
        otpr=Products.objects.filter(~Q(id=id))
        otpro=otpr.filter(cname_id=pro[0].cname_id)
        
         
        return render(request,'pd.html',{'pro':pro,'otpro':otpro})
   
    else:
        messages.warning(request,"NOT Found")
        return redirect('pro')

    
   
       
   
   
    

 
    




