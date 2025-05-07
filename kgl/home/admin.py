from django.contrib import admin
#Accessing our own models
from .models import *
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Sale)
admin.site.register(Stock)
admin.site.register(Category)
admin.site.register(Procurement)
