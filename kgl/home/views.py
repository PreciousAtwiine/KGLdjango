from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#Imports all the models from the models.py file in the same directory
from .models import *
#Accessing all our models
from django.urls import reverse
from .forms import *
from django.shortcuts import redirect
#Borrowing the functionality of inbuilt/existing user from django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home_view(request):
    render(request,'homeapp/index.html')
#View for index page
def index(request):
    stocks = Stock.objects.all().order_by('-id')
    return render (request, "homeapp/index.html", {'stocks':stocks})

def navbar(request):
    return render (request, "homeapp/navbar.html")

#View for receipt page
# @login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'homeapp/receipt.html', {'sales':sales})

#View for add sales
@login_required
def addsales(request):
    return render(request, 'homeapp/addsales.html')

#View for add stock

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
    return render(request, "homeapp/sales.html")

#View for allstock
def allstock(request):
    return render(request, "homeapp/stock.html")

#View to handle a link for a particular item 
def stockdetail(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    return render(request, 'homeapp/stockdetail.html', {'stock': stock})

def issue_item(request,pk):
    #creating a variable to hold the item to be issued and access all entries in the stock table by their id
    issued_item = Stock.objects.get(id=pk)
    #Accessing our form from forms.py
    sales_form = AddSaleForm(request.POST)
    #Checking if the request method is post and the form is valid
    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item_name = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #To keep track of the quantity of the item in stock after issuing it
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            return redirect('receipt')
        return render(request, 'homeapp/issue_item.html',{'sales_form': sales_form, 'issued_item': issued_item})
def receipt_detail(request, receipt_id):
    receipt= Sale.objects.get(id=receipt_id)
    return render(request, 'homeapp/receipt_detail.html', {'receipt': receipt})

#View for logging in
def Login(request):
    form = AuthenticationForm()
    return render(request, 'homeapp/login.html', {'form': form})
    
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
        
    #     if user is not None and user.is_owner== True:
    #         form = login(request,user)
    #         return redirect('/dasboard1')
    #     if user is not None and user.is_manager== True:
    #         form = login(request,user)
    #         return redirect('/dashboard2')
    #     if user is not None and user.is_salesagent== True:
    #         form = login(request,user)
    #         return redirect('/dashboard3')
    #     else:
    #         print("Sorry! something went wrong")
    #         form = AuthenticationForm()
    #         return render(request, 'homeapp/login.html', {'form': form})
        
        
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
            return render(request, 'homeapp/signup.html', {'form': form})
def manager(request):
    return render(request, 'homeapp/dashboard2.html')

def salesagent(request):
    return render(request, 'homeapp/dashboard3.html')       
        
        
    
