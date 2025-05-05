"""
URL configuration for kgl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Accessing the views file in our application
from home import views
from home.views import home_view
#borrowing the functionality of login from django
from django.contrib.auth import views as auth_views
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home_view, name='home'),
    path('', views.Login, name='login'),
    
    #Below is the url for the index page
    #path('home/',views.index, name='index'),
    
    #Below is the url for the receipt page
    path('receipt/',views.receipt, name='receipt'),
    #URL for addsales page
    path('addsales/<str:pk>/',views.addsales, name='addsales'),
    #URL for allsales page
    path('sales/',views.allsales, name='allsales'),
    #URL for allstock page
    path('stock/',views.allstock, name='allstock'),
    #URL for addstock page
    path('addstock/<int:pk>/',views.addstock, name='addstock'),
    #URL for stockdetail page
    path('stockdetail/<int:stock_id>/',views.stockdetail, name='stockdetail'),
    
    #Handling a url for a particular url checkout item
    path('home/<int:stock_id>/', views.stockdetail, name='stockdetail'),
    # handling a url for a particular sell item
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('navbar/',views.navbar, name='navbar'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('login/',auth_views.LoginView.as_view(template_name='homeapp/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='homeapp/logout.html'), name='logout'),
    path('login/', views.Login, name='login'),
    # url for signup page
    path('signup/', views.signup, name='signup'),
    path('dashboard1/', views.index, name= 'index'),
    #url for manager
    path('dasboard2/', views.manager, name='manager'),
    #url for sales agent
    path('dashboard3/', views.salesagent, name='salesagent')
    
    
    
]
