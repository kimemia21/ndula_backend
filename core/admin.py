from django.contrib import admin
from .models import Shoe,BrandName,Cart,CartItem
# from django.contrib.auth.models import User

admin.site.register([Shoe,BrandName,Cart,CartItem])


# Register your models here.
