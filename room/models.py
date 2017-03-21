from django.db import models

# Create your models here.
class Room(models.Model):
	GAME_TYPES=(("SP","Simpleplay"),("MP","Multiplay"))
	game_type = models.CharField(max_length = 3,choices = GAME_TYPES)

	name = models.CharField(max_length=50)
	date_begin=models.DateField(auto_now =True)
	date_end=models.DateField(blank=True)
