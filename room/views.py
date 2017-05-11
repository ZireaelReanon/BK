# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from .models import Room,Character
import random
# Create your views here.
# Функция для перехода на шаблон комнаты
def go_to_room(request, id=None):
    instance = get_object_or_404(Room, id=id)
    players = Character.objects.filter(room=instance)
    context = {
		"instance": instance,
        "players": players,
	}
    return render(request, "fight_room.html", context)
@csrf_protect
def show_rooms(request):
	# В случае если метода POST
	if request.method == "POST":
		# получаем данные из запроса
		name_room = request.POST.get("nameRoom")
		name_player = request.POST.get("nameChar")
		race_player = request.POST.get("raceChar")
		name_enemy = request.POST.get("nameEnem")
		race_enemy = request.POST.get("raceEnem")
		# Создаем комнату и сохраняем ее в базе данных
		room = Room(name=name_room,game_type = "SP")
		room.save()
		# Создаем игрока и врага, далее сохранияе в базе данных
		players = Character(room=room, name = name_player, race =race_player)
		enemy = Character(room=room, name = name_enemy, race =race_enemy)
		players.save()
		enemy.save()
		# Переходим на страницу с комнаты.
		return HttpResponseRedirect(room.get_absolute_url())
	rooms = Room.objects.all()
	characters = Character.objects.all()
	context = {
		"title":"Rooms",
		"rooms": rooms,
		"characters":characters,
		# Добавила поле races для правильного отображения расы
		"races":Character.RACE
	}
	return render(request,"main_menu.html",context)
def create_players(request):
	context = {
		"title":"Create players",
		"races":Character.RACE	
	}
	return render(request,"characters_create.html", context)
def fight_room(request):
	context = {"title":"Fight room"}
	return render(request,"fight_room.html", context)
def attack(request):
	if request.is_ajax():
		# Получить id от запроса
		player_id = request.GET.get("playerId")
		enemy_id = request.GET.get("enemyId")
		# совершить поиск в базе по id, чтобы найти персонажа
		player = Character.objects.get(id=player_id)
		enemy = Character.objects.get(id=enemy_id)
		part_enemy = request.GET.get("partEnemy")
		part_player = request.GET.get("partPlayer")
		enemy.choice_target(random.randint(0,4))
		enemy.body_block(random.randint(0,4))
		player.choice_target(int(part_enemy))
		player.body_block(int(part_player))
		enemy.attack(player)
		player.attack(enemy)
		# Завершить атаку 


		# Сохранить новые значения в базе данных
		enemy.save()
		player.save()
		context = {
			"healthEnemy": enemy.health,
			"healthPlayer": player.health
		}
		jsresp = JsonResponse(context)
		return HttpResponse(jsresp.content, content_type='text/html')
		return HttpResponseRedirect(room.get_absolute_url()) 
