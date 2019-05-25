from django.urls import path, re_path
from .views import index, room

app_name = 'chat'

urlpatterns= [
    path("", index, name="index"),
    path('<room_name>/', room, name='room'),
]