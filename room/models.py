from django.db import models

# Create your models here.
class Room(models.Model):
	GAME_TYPES=(("SP","Simpleplay"),("MP","Multiplay"))
	game_type = models.CharField(max_length = 3,choices = GAME_TYPES)
	name = models.CharField(max_length=50)
	date_begin=models.DateField(auto_now =True)
	date_end=models.DateField(blank=True, null=True)

def __str__(self):
	return self.name

class Character(models.Model):
	RACE=(("DE","Dark Elf"),("OR","Orc"),("MG","Magician"),("HU","Human"),("DW","Dwarf"),("W","Werewolf"),("DR","Driada"))
	room= models.ForeignKey(Room)
	name=models.CharField(max_length=50)
	race=models.CharField(max_length = 6,choices = RACE)
	BODY_PARTS=["Head","Torso","Left hand","Right hand","Legs"]
	health = 100
	
def __str__(self):
	return self.name

def hit(self,target):
		health = self.health
		if target == 0:
			self.health -= 50
		elif target == 1:
			self.health-= 40
		elif 2 <= target <= 3:
			self.health -= 10
		elif target == 4:
			self.health -= 20
def attack(self,enemy):
	print(enemy.block_part)
	if self.target != enemy.block_part:
			enemy.hit(self.target)
def choice_target(self, target):
	self.target = target
def body_block(self,block_part):
	self.block_part = block_part
