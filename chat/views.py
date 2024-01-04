from django.shortcuts import render

# Create your views here.

# TODO https://channels.readthedocs.io/en/stable/tutorial/part_1.html#add-the-index-view
def index(request):
    return render(request, "chat/index.html")

# TODO https://channels.readthedocs.io/en/stable/tutorial/part_2.html#add-the-room-view
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})