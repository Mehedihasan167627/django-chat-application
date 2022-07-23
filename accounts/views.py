
from django.contrib.auth import login,logout,authenticate
from django.views import View 
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser

from .models import CustomUser
import uuid


class LoginView(View):
    return_url=""
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("pages:home")
        LoginView.return_url=request.GET.get("return_url")
        return render(request,'accounts/login.html')
    
    def check_email(self,email):
        return CustomUser.objects.filter(email=email)
    

        
    def post(self,request):
        email=request.POST.get("email")
        password=request.POST.get("password")
        if not self.check_email(email):
            messages.warning(request,"You are not a Customer!!")
            return redirect("accounts:login")

        url_check=False 
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You're logged in successfully!!")
            if LoginView.return_url:
                return redirect(f"{LoginView.return_url}")
               
            else:
                return redirect("chat:chat-home")    
        else:
            messages.warning(request,"Email or password is incorrect!!")
            if LoginView.return_url:
                url_check=LoginView.return_url
            return render(request,'accounts/login.html',{"email":email,"url_check":url_check})

class RegisterView(View):
    def get(self,request): 
        if request.user.is_authenticated:
            return redirect("pages:home")
        return render(request,"accounts/register.html")
    def post(self,request):
        email=request.POST.get("email")
        password=request.POST.get("password")
        password=request.POST.get("password")
        email_check=CustomUser.objects.filter(email=email)

        if not email_check:
            user=CustomUser(
                username="",
                email=email,
                password=make_password(password),
                token=str(uuid.uuid4())[:100].replace("-","")+str(uuid.uuid4())[:140].replace("-",""),
                is_active=True 
                )

            user.save()
            if user:
                messages.success(request,"Your account created successfully!!")
                return redirect("accounts:login")
        else:
            messages.warning(request,"Email address already exists!!!")
            return redirect("accounts:register")





class LogoutView(View):
    def get(self,request): 
        logout(request)
        messages.success(request,"You're logged out successfully!!")
        return redirect("accounts:login")

