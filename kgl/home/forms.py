from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Accessing ModelForm from django
from django.forms import ModelForm
#accessing our models to create corresponding forms
#Importing all forms
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=30,required=True)
    lastname = forms.CharField(max_length=30,required=True)
    
    class Meta:
        model = User
        fields=('username','firstname','lastname','email','password1','password2')

#Form for adding sales
class AddSaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
#Form for adding procurement
class AddProcurementForm(ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'
        def save(self, commit=True):
            procurement = super(AddProcurementForm, self).save(commit=False)
           
            if commit:
                procurement.save()
            return procurement
class UpdateStockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        def save(self, commit=True):
            stock = super(UpdateStockForm, self).save(commit=False)
            if commit:
                stock.save()
            return stock        
        