
from django.conf import settings
from django.contrib import admin
from django.urls import path,include 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls",namespace="accounts")),
    path('chat/',include("chat.urls",namespace="chat")),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)