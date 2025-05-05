#Accessing ModelForm from django
from django.forms import ModelForm
#accessing our models to create corresponding forms
#Importing all forms
from .models import *

#form for adding a new user
class UserForm(ModelForm):
    class Meta:
        model = Userprofile
        fields = '__all__'
        def save(self, commit=True):
            user = super(UserForm, self).save(commit=False)
            # Set the password using the set_password method
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
#Form for adding sales
class AddSaleForm(ModelForm):
    class Meta:
        model = Procurement
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
        