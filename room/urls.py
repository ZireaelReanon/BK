from django.conf.urls import url
from .views import show_room
urlpatterns = [
    url(r'^main_menu/',show_room)
    
]