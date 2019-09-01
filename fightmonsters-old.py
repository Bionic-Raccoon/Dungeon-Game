import random
import time
from time import sleep

name = input("Welcome to the adventure!  Enter your new character's name:")
print ("Your new characters is named " + name)
strength = random.randint(0,3)
dexterity = random.randint(0,3)
constitution = random.randint(0,3)
hitpoints = random.randint(5,10) + constitution

print ("Here are your stat modifiers:")
sleep(1)
print ("Strength: " + str(strength))
sleep(1)
print ("Dexterity: " + str(dexterity))
sleep(1)
print ("Constitution: " + str(constitution))
sleep(1)
print ("Hit Points: " + str(hitpoints))
sleep(2)

goblinkills = 0

print ("\nYou enter the dungeon!")

def fightgoblin(hitpoints = 0, goblinkills=0):
	goblinhp = random.randint(1,12)
	print ("You see a goblin!")
	sleep(1)
	print ("He has " + str(goblinhp) + " hit points!")
	sleep(1)
	while goblinhp > 0:
		attack = input("Do you want to attack? (y/n)")
		if attack == 'y':
			print ("You try and hit the goblin!")
			sleep(1)
			tohit = random.randint(1,20)
			print ("You roll a " + str(tohit) + "!!!!")
			sleep(1)
			if tohit > 12:
				print ("You hit the goblin!")
				damage = random.randint(1,12) + strength
				goblinhp = goblinhp - damage
				if goblinhp < 1:
					print ("You killed him!")
					sleep (1)
					goblinkills = goblinkills + 1
					return [hitpoints, goblinkills]
				else:
					print("You hit for " + str(damage) + ", the goblin, it has " + str(goblinhp) + " hit points left")
			else:
				print ("Your pitiful attempt fails!  You miss the goblin!")
				sleep(1)
		print ("The goblin tries to smite you!")
		if random.randint(1,20) > 10 + dexterity:
			goblindamage = random.randint(1,5)
			print ("The goblin hits you for " + str(goblindamage) + " damage")
			hitpoints = hitpoints - goblindamage
			print ("You have " + str(hitpoints) + " hit points left!")
			sleep(1)
			if hitpoints < 1:
				return [hitpoints, goblinkills]
		else:
			print ("The goblin misses you!")
			sleep(1)
while hitpoints > 0:
	[hitpoints, goblinkills] = fightgoblin(hitpoints, goblinkills)
	print ("You have killed " + str(goblinkills) + " goblins!")
	sleep(1)
if goblinkills > 0:
	print ("Sorry, you died! But you killed " + str(goblinkills) + "!\n so there's that...")
else:
	print ("You got 0 kills and there is no justifing that!")
