"""
ASGI config for main_settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_settings.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
           routers.ws_patterns
       )
    ),

})