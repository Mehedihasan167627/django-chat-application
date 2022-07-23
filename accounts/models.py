
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserModel

class CustomUser(AbstractUser):
    username=models.CharField(max_length=100,blank=True,null=True) 
    email=models.EmailField(unique=True) 
    profile_picture=models.ImageField(upload_to="accounts/uploads/profiles",
           default="accounts/uploads/no_avatar.png")
    token=models.CharField(max_length=255,blank=True,null=True)
    verify=models.BooleanField(default=False)
    objects=UserModel()
    
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]


  