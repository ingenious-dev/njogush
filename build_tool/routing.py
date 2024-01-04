# build_tool/routing.py

# TODO https://channels.readthedocs.io/en/stable/tutorial/part_2.html#write-your-first-consumer
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/build/(?P<room_name>\w+)/$", consumers.BuildConsumer.as_asgi()),

    # then room name could contain hyphen e.g UUID
    re_path(r"ws/build/(?P<room_name>[\w-]*)/$", consumers.BuildConsumer.as_asgi()),
]