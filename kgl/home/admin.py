from django.contrib import admin
#Accessing our own models
from .models import *
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Procurement)
admin.site.register(Sale)
admin.site.register(Stock)
