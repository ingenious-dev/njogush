# chat/urls.py
# TODO https://channels.readthedocs.io/en/stable/tutorial/part_1.html#add-the-index-view
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"), # TODO https://channels.readthedocs.io/en/stable/tutorial/part_2.html#add-the-room-view
]