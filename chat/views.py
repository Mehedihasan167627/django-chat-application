from django.http import HttpResponse
from django.shortcuts import render
from django.views import View 
from accounts.models import CustomUser

from chat.models import Chat 

class ChatIndexView(View):
    def get(self,request):
        user=CustomUser.objects.all()
        return render(request,"chat/index.html",{"user_list":user})

class ChatView(View):
    def get(self,request,token):
        user=CustomUser.objects.all()
        try:
            friend=CustomUser.objects.get(token=token)
        except:
            return HttpResponse("invalid url!!")
        message_list=Chat.get_messages(request.user,friend)
        context={
            "friend":friend,
            "user_list":user,
            "message_list":message_list
            }
 
        return render(request,"chat/chat.html",context)