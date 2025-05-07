from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
#Imports all the models from the models.py file in the same directory
from home.models import *
#Accessing all our models
from django.urls import reverse
from .forms import *
from django.shortcuts import redirect

#Borrowing the functionality of inbuilt/existing user from django
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


#View for logging in
def Login(request):
    form = AuthenticationForm()
    #return render(request, 'homeapp/login.html', {'form': form})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_owner== True:
            form = login(request,user)
            return redirect('/dashboard')
        if user is not None and user.is_manager== True:
            form = login(request,user)
            return redirect('/dashboard')
        if user is not None and user.is_salesagent== True:
            form = login(request,user)
            return redirect('/dashboard')
        else:
            print("Sorry! something went wrong")
            form = AuthenticationForm()
            return render(request, 'homeapp/login.html', {'form': form})
@login_required
def dashboard(request):
    return render(request,'dashboard/dash.html') 
@login_required
def Home(request):
    return render(request,'homeapp/home.html',{'page':'Home'}) 
@login_required
def About(request):
    return render(request, 'homeapp/introduction.html', {'page':'About'}) 

def Contact(request):
    return render(request,'homeapp/contact.html',{'page':'Contact' })
def Products(request):
    return render(request,'homeapp/products.html',{'page':'Products'})

def Dashboard_Products(request):
    return render(request,'Dash/products.html',{'page':'products'})

def Dashboard_Sales(request):
    
    context = {
        'sales': Sale.objects.all()
    }
    return render(request,'Dash/sales.html',context)

def Dashboard_Stock(request):
    #stock = Stock.objects.all()
    context = {
        'stock': Stock.objects.all()
    }
    return render(request,'Dash/stock.html',context)



def Dashboard_Users(request):
    users = Userprofile.objects.all()
    context = {
        'users': users
    }
  
    #users = Userprofile.objects.all().order_by('-id')
    return render(request,'Dash/users.html',context)

def Dashboard_Userdetail(request,user_id):
    Userprofile = get_user_model()
    user = get_object_or_404(Userprofile,id=user_id)
    # context = {
    #     'user': user,
    #     'page_title': f"{user.username}'s Profile"
    # }
    return render(request,'Dash/userDetails.html',{'user':user})
    
def Dashboard_Logout(request):
    return render(request,'Dash/logout.html')  
#View for stock page
def stock(request):
    context = {
        'stocks':Stock.objects.all()
        
    }
    #Getting all the registered stock from our database
    
    return render (request, "homeapp/stock.html", context)


#View for add sales
@login_required
def addsales(request):
    return render(request, 'homeapp/addsales.html')

#View for add stock
@login_required
def addstock(request,pk):
    issued_item = Stock.objects.get(id=pk)
    form = UpdateStockForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            #To add to the initial quantity of the item in stock
            issued_item.total_quantity += added_quantity
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('index')
        return render(request, "homeapp/addstock.html")
#View for all sales
def allsales(request):
    sales = Sale.objects.all()
    context = {
        'sales':sales
    }
    return render(request, "homeapp/sales.html",context)

#View for allstock
def allstock(request):
    stock = Stock.objects.all()
    context = {
        'stock':stock
    }
    return render(request, "homeapp/stock.html",context)



   


def users(request):
    users = Userprofile.objects.all()
    context = {
        'users': users
    }
    
    return render(request,'homeapp/users.html',context) 
@login_required
def userdetail(request,user_id):
    Userprofile = get_user_model()
    user = get_object_or_404(Userprofile,id=user_id)
    # context = {
    #     'user': user,
    #     'page_title': f"{user.username}'s Profile"
    # }
    return render(request,'homeapp/userDetails.html', {'user': user})
        
        
#view for signup page
def signup(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            return redirect('/login')
        else:
            form = UserCreationForm()
            return render(request, 'homeapp/signup.html', {'form': form},{'page_title': "KGL system | Signup",'page':'Signup'})
def manager(request):
    return render(request, 'homeapp/dashboard2.html')

def salesagent(request):
    return render(request, 'homeapp/dashboard3.html')   


        
        
    
