from django.urls import path
from . import views
from home import views
app_name = 'home'
#borrowing the functionality of login from django
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('',auth_views.LoginView.as_view(template_name='homeapp/login.html'), name='login'),
    #URL for dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    #Dashboard products
    path('dashboard/products', views.Dashboard_Products, name='products'),
    #Dashboard users
    path('dashboard/users', views.Dashboard_Users, name='users'),
    path('dashboard/users/<int:user_id>/', views.Dashboard_Userdetail, name='Dashboard_Userdetail'),
    #Dashboard stock
    path('dashboard/stock', views.Dashboard_Stock, name='stock'),
    #Dashboard sales
    path('dashboard/sales', views.Dashboard_Sales, name='sales'),
    #Logout
    path('dashboard/logout',views.Dashboard_Logout,name='logout'),
    
       
    
    
    #URL for addsales page
    path('addsales/<str:pk>/',views.addsales, name='addsales'),
    #URL for allsales page
    path('sales/',views.allsales, name='allsales'),
    #URL for allstock page
    path('stock/',views.allstock, name='allstock'),
    #URL for addstock page
    path('addstock/<int:pk>/',views.addstock, name='addstock'),
        #Url for users
    path('users/',views.users, name='users'),
    #path for user detail
    path('details/<int:user_id>/',views.userdetail,name='userdetail'),
    #path('users/<int:user_id>/', views.userdetail, name='userdetail'),
    path('login/',auth_views.LoginView.as_view(template_name='homeapp/login.html'), name='login'),
    #path('logout/',auth_views.LogoutView.as_view(template_name='homeapp/logout.html'), name='logout'),
    # url for signup page
    path('signup/', views.signup, name='signup'),
    path('dashboard1/', views.Dashboard_Users, name= 'dashboard1'),
    #url for manager
    path('dasboard2/', views.manager, name='manager'),
    #url for sales agent
    path('dashboard3/', views.salesagent, name='salesagent'),
    
    path('contact/', views.Contact, name="contact"),
    path('introduction/', views.About, name="about"),
    path('products/', views.Products,name='products'),
    
    
    
    
    
]
