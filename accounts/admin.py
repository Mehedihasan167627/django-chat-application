from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserModel(UserAdmin):
    list_display=["email","verify","token","is_active",'is_staff',"is_superuser"]
admin.site.register(CustomUser,UserModel)

