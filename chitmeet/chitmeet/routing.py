from django.urls import path, re_path
from chat.consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r"^chat/(?P<username>[\w.@+-]+)/$", ChatConsumer.as_asgi()),
    # path("chat/sambit/", ChatConsumer.as_asgi()),
]