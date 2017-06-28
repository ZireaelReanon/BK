import random;
class Character_Demo:

	BODY_PARTS=["Head","Torso","Left hand","Right hand","Legs"]

	health = 100
	health_shield = 100
	state = False

	def __init__ (self, name, race):
		self.name = name
		self.race = race
		
	def hit(self,target):
		if target==0:
			self.health -= 50
		elif target == 1:
			self.health -=40
		elif 2<= target <=3:
			self.health-=10
		elif target == 4:
			self.health-=20

	def attack(self,enemy):
		if self.target!=enemy.block_part:
			enemy.hit(self.target)

	def choice_target(self,target):
		self.target = target 

	def body_block(self,block_part):
		self.block_part=block_part

#orc = Character_Demo ("Carl","orc")
#name = input ("Whats your name?:")
#race = input ("Input race:")
#player = Character_Demo (name,race)
#exit = False


#while True:
	#if (player.health <=0) or (orc.health<=0) or (exit):
		#print("GameOver")
		#break
	#else:
		#target = input("Choose target attack: ")
		#block_part=input("Choose your block part: ")

		#if target == "Exit" or block_part =="Exit":
			#exit = True
		#else:
			#orc.choice_target(random.randint(0,4))
			#orc.body_block(random.randint(0,4))

			#player.choice_target(Character_Demo.BODY_PARTS.index(target))
			#player.body_block(Character_Demo.BODY_PARTS.index(block_part))

			#orc.attack(player.target)
			#player.attack(orc.target)

		#print("Player")
		#print("Target:",player.BODY_PARTS[player.target])
		#print("Target:",player.BODY_PARTS[player.block_part])
		#print("Health:",player.health)

		#print("Orc")
		#print("Target:",orc.BODY_PARTS[orc.target])
		#print("Target:",orc.BODY_PARTS[orc.block_part])
		#print("Health:",orc.health)

















