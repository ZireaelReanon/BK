# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from .models import Room, Character
import random
from datetime import datetime, date # models.py / characters.create.html )data end block
from django.urls import reverse
from .character import Character_Demo
# Create your views here.
player = Character_Demo("MAMBA","Ork")
enemy = Character_Demo("HEEEEH","Wolf")
# Функция для перехода на шаблон комнаты
def go_to_room(request, id=None):
	instance = get_object_or_404(Room, id=id)
	# status = True
	# print(instance.data_end)
	# if instance.data_end:
	# 	return redirect(reverse("arena:result", kwargs={"id": instance.id}))
	players = Character.objects.filter(room=instance)
	#print('players = %s ' %players)
	context = {
		"instance": instance,
		"players": players,
		"title":"fight-room"
		# "status": status,
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

		return HttpResponseRedirect(Room.get_absolute_url(request))
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
	global player, enemy
	if request.is_ajax():
		# Получить id от запроса
		p_id=request.GET.get('roomId')
		#print(p_id)# получаем от запроса пользователя данные и отправляем их на сервер  и преобразоват в переменную
		room=Room.objects.get(id=p_id)# jобр строку найдет обект комната в базе рум и возворащается обект рум
		#в комнате ест поля игрок комната начало конец 
		player_id = request.GET.get("playerId")
		enemy_id = request.GET.get("enemyId")
		r_id = request.GET.get("roomId")
		# совершить поиск в базе по id, чтобы найти персонажа
		# player = Character.objects.get(id=player_id)
		# enemy = Character.objects.get(id=enemy_id)
		part_enemy = request.GET.get("partEnemy")
		part_player = request.GET.get("partPlayer")
		enemy.choice_target(random.randint(0,4))
		enemy.body_block(random.randint(0,4))
		player.choice_target(int(part_enemy))
		player.body_block(int(part_player))
		enemy.attack(player)
		player.attack(enemy)
		print("Player")
		print("Target:", player.BODY_PARTS[player.target])
		print("Block:", player.BODY_PARTS[player.block_part])
		print("Health:", player.health)
		print("enemy")
		print("Target:", enemy.BODY_PARTS[enemy.target])
		print("Block:", enemy.BODY_PARTS[enemy.block_part])
		print("Health:", enemy.health)

		# Завершить атаку 
#в дате тег с id 
		# Сохранить новые значения в базе данных
		# enemy.save()
		# player.save()
		# room.save()
		if enemy.health <=0 or player.health <=0 :
			context = fight_result(enemy.health, player.health, p_id)
			print("context = %s" % context)
			# room.data_end=datetime.now()
			# room.save()
			jsresp = JsonResponse(context)
			return HttpResponse(jsresp, content_type='text/html')
			#return HttpResponseRedirect("finish_base.html", context)
			#return HttpResponseRedirect(Character.get_result(request))
		context = {
			"healthEnemy": enemy.health,
			"healthPlayer": player.health,
		}
		jsresp = JsonResponse(context)
		return HttpResponse(jsresp.content, content_type='text/html')
	#поле для models.py


def fight_result(enemy, player, p_id):
	print('p_id = %s' %p_id)
	room = Room.objects.get(id=p_id)
	players = Character.objects.filter(room=room)
	if player < enemy:
		resultstr = 'Enemy %s Win! Sorry you are lost!' % players[1]
		character_vin = players[1]
		print(character_vin)
	elif player > enemy:
		resultstr = 'Player %s win! You best!!!' % players[0]
		character_vin = players[0]
		print(character_vin)
	elif player == enemy:
		resultstr = 'Congratulate, win friendship!'
		character_vin ='friendship'
	print("result = %s" %resultstr)
	context = {
		"result": resultstr,
		"character_vin": character_vin.name,
	}
	# #return HttpResponseRedirect(room.get_absolute_url(), date.today())
	return context
	# return HttpResponseRedirect("finish_base.html" , context)

def result(request):
	context = {'title': "Fisnish",
			   }
	return render(request, "finish_base.html", context)