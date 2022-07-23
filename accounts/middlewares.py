from django.contrib import messages
from django.shortcuts import redirect

def customer_middleware(get_response):
    def middleware(request):
        return_url=request.META["PATH_INFO"]   
        print(return_url) 
        if request.user.is_authenticated==False:
            messages.warning(request,"Please Login with your account")
            return redirect(f"/accounts/login/?return_url={return_url}")
   
        response=get_response(request)
        return response

    return middleware
def customer_middleware_with_id(get_response):
    def middleware(request,token=None):
        return_url=request.META["PATH_INFO"]   
        print(return_url) 
        if request.user.is_authenticated==False:
            messages.warning(request,"Please Login with your account")
            return redirect(f"/accounts/login/?return_url={return_url}")
   
        response=get_response(request,token)
        return response

    return middleware
