
from django.urls import path
from .views import ChatView,ChatIndexView
from accounts.middlewares import customer_middleware,customer_middleware_with_id

app_name="chat"
urlpatterns = [
     path("",customer_middleware(ChatIndexView.as_view()),name="chat-home"),
     path("<slug:token>/",customer_middleware_with_id(ChatView.as_view()),name="chat-room"),
]
