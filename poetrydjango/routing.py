from bridger.notifications.consumers import NotificationConsumer
from bridger.websockets.auth import JWTAuthMiddlewareStack
from bridger.websockets.consumers import \
    AsyncAuthenticatedJsonWebsocketConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path

websocket_urlpatterns = [
    path("ws/socket/", AsyncAuthenticatedJsonWebsocketConsumer),
    path("ws/notification/", NotificationConsumer),
]

application = ProtocolTypeRouter(
    {"websocket": JWTAuthMiddlewareStack(URLRouter(websocket_urlpatterns))}
)
