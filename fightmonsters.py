import random

print ("Welcome to the adventure!  Enter your new character's name:")
name = raw_input()
print ("Your new characters is named " + name)
strength = random.randint(0,3)
dexterity = random.randint(0,3)
constitution = random.randint(0,3)
hitpoints = random.randint(5,10) + constitution

print ("Here are your stats:")
print ("Strength: " + str(strength))
print ("Dexterity: " + str(dexterity))
print ("Constitution: " + str(constitution))
print ("Hit Points: " + str(hitpoints))

goblinkills = 0

print ("\nYou enter the dungeon!")

def fightgoblin(hitpoints = 0, goblinkills=0):
	goblinhp = random.randint(1,12)
	print ("You see a goblin!")
	print ("He has " + str(goblinhp) + " hit points!")
	while goblinhp > 0:
		print ("Do you want to attack? (y/n)")
		attack = raw_input()
		if attack == 'y':
			print ("You try and hit the goblin!")
			tohit = random.randint(1,20)
			print ("You roll a " + str(tohit) + "!!!!")
			if tohit > 12:
				print ("You hit the goblin!")
				damage = random.randint(1,12) + strength
				goblinhp = goblinhp - damage
				if goblinhp < 1:
					print ("You killed him!")
					goblinkills = goblinkills + 1
					return [hitpoints, goblinkills]
				else:
					print("You hit for " + str(damage) + ", the goblin, it has " + str(goblinhp) + " hit points left")
			else:
				print ("Your pitiful attempt fails!  You miss the goblin!")
		print ("The goblin tries to smite you!")
		if random.randint(1,20) > 10 + dexterity:
			goblindamage = random.randint(1,5)
			print ("The goblin hits you for " + str(goblindamage) + " damage")
			hitpoints = hitpoints - goblindamage
			print ("You have " + str(hitpoints) + " hit points left!")
			if hitpoints < 1:
				return [hitpoints, goblinkills]
		else:
			print ("The goblin misses you!")

while hitpoints > 0:
	[hitpoints, goblinkills] = fightgoblin(hitpoints, goblinkills)
	print ("You have killed " + str(goblinkills) + " goblins!")
	
print ("Sorry, you died! But you killed " + str(goblinkills) + "!\n so there's that...")
