from django.db import models
#For minimum length
from django.core.validators import MinLengthValidator
#Borrowing the functionality of inbuilt/existing user from django
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

class Userprofile(AbstractUser):
    is_salesagent = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address=models.TextField(max_length=50, blank=True)
    gender = models.TextField(max_length=50, blank=True)
    phonenumber = models.CharField(max_length=15, blank=True, unique=True)
    
    # Override default reverse accessors to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="userprofile_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="userprofile_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )
    #is meant for reference purpose specifying username to be used as a reference for each individual object/record in the table
    def __str__(self):
        return self.username
    #Displays username in admin panel
# Table for procurement
class Procurement(models.Model):
    product_name = models.TextField(null=False, blank=False)
    product_code = models.TextField(null=False, blank=False)
    product_description = models.TextField(null=False, blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    product_quantity = models.IntegerField(null=False, blank=False)
    product_supplier = models.TextField(null=False, blank=False)
    

class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True, blank=True)
    def _str_(self):
        return self.category_name
# Table for stock
class Stock(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    
    item_name = models.CharField(max_length= 50, null=False, blank=False)
    product_description = models.TextField(null=False, blank=False)
    cost = models.FloatField(default = 0, null = True, blank=False)
    unit_price = models.FloatField(default = 0, null=False, blank=False)
    unit_cost = models.FloatField(default = 0, null=False, blank=False)
    total_quantity = models.IntegerField(default = 0,null=False, blank=False)
    received_quantity = models.IntegerField(default = 0,null=False, blank=False)
    tyep_of_stock = models.CharField(max_length=20)
    product_supplier = models.TextField(null=False, blank=False)   
    date = models.DateField(auto_now_add = True)  
    def _str_(self):
        return self.item_name  

class Sale(models.Model):
    product_name = models.ForeignKey(Stock, on_delete= models.CASCADE, null=False, blank=False)
    unit_price = models.FloatField(default=0, null=False, blank=False)
    quantity = models.IntegerField(default = 1,null=False, blank=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    product_supplier = models.TextField(null=False, blank=False)
    customer_name = models.CharField(max_length = 80)
    customer_phone_number = models.CharField(max_length=15, null=False, blank=False)
    amount_received = models.FloatField(default=0, null=False, blank=False)
    payment_method = models.CharField(choices= [('Cash','Cash'),('Mpesa','Mpesa'),('Bank Transfer','Bank Transfer')], default = 'Cash', max_length=20, null=False, blank=False)
    
    def get_total(self):
        return int(self.unit_price* self.quantity)
    def get_change(self):
        return abs(int(self.get_total() - self.amount_received))
    def __str__(self):
        return self.customer_name
    
       
        