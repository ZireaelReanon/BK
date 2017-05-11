from django.conf.urls import url
from .views import (show_rooms,create_players,fight_room, attack,go_to_room)

urlpatterns = [
    url(r'^main/$', show_rooms),
    url(r'^create_players/$', create_players ),
    url(r'^fight_room/$', fight_room ),
    # Добавлена страница шаблон для комнаты. И имя для заполнения аргумента функции reverse()
    url(r'^(?P<id>[\w-]+)/game$', go_to_room, name="in_room"),
    url(r'^attack/$', attack ),

]