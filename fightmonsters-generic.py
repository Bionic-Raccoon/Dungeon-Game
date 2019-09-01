import random
import time
from time import sleep



def statdescriptor(stat):
	if stat == 3:
		return "very"
	elif stat == 2:
		return "sort of"
	elif stat == 1:
		return "kind of"
	else:
		return "not very"

def fightmonster(monster="", monstermaxhp=1, monsterac = 10, monsterxp=0, monsterdamage=1, hitpoints=0, kills=0, xp=0):
	# This is a generic fight function, you can tell it what to fight
	monsterhp = random.randint(1,monstermaxhp)
	print ("You encounter a " + monster + "!")
	sleep(1)
	print ("It has " + str(monsterhp) + " hit points!")
	print ("You have " + str(hitpoints) + "  hit points!")
	while monsterhp > 0 and hitpoints > 0:
		attack = input("Do you want to attack? (y/n)")
		sleep(1)
		if attack == 'y':
			print ("You try and hit the " + monster+ "!")
			sleep(1)
			tohit = random.randint(1,20) + strength
			print ("You roll a " + str(tohit) + "!!!!")
			sleep(1)
			if tohit > monsterac:
				print ("You hit the " + monster + "!")
				sleep(1)
				damage = random.randint(1,12) + strength
				monsterhp = monsterhp - damage
				if monsterhp < 1:
					print ("You killed the " + monster + "!")
					sleep(1)
					kills = kills + 1
					xp = xp + monsterxp
					break
				else:
					print("You hit for " + str(damage) + ", the " + monster + ", it has " + str(monsterhp) + " hit points left")
					sleep(1)
			else:
				print ("Your pitiful attempt fails!  You miss the " + monster + "!")
				sleep(1)
		else:
			# This is if you don't enter 'y' when asked if you want to attack
			print("You try and get away!")
			escape = random.randint(1,10) + dexterity
			if escape > 5:
				print ("You get away!")
				return [hitpoints, kills, xp]
			else:
				print("The " + monster + " is too fast, you can't get away!")
		print ("The " + monster + " tries to smite you!")
		sleep(1)
		if random.randint(1,20) > 10 + dexterity:
			damage = random.randint(1,monsterdamage)
			print ("The " + monster + " hits you for " + str(damage) + " damage!")
			sleep(1)
			hitpoints = hitpoints - damage
			print ("You have " + str(hitpoints) + " hit points left!")
			sleep(1)
		else:
			print ("The " + monster + " misses you!")
			sleep(1)
	return [hitpoints, kills, xp]

def fightspider(hitpoints = 0, spiderkills = 0, xp = 0):
	#put the spider fighting code in here
	[hitpoints, spiderkills, xp] = fightmonster("giant spider", 15, 13, 40, 8, hitpoints, spiderkills, xp)
	return [hitpoints, spiderkills, xp]

def fightgoblin(hitpoints = 0, goblinkills=0, xp=0):
	[hitpoints, goblinkills, xp] = fightmonster("goblin", 10, 12, 25, 6, hitpoints, goblinkills, xp)
	return [hitpoints, goblinkills, xp]
	
# The program actually starts here!
name = input("Welcome to the adventure!\nEnter your new character's name: ")
print ("Your new characters is named: " + name)
sleep(1)

# Easter egg
if name == "Fodor":
	print("Hello Dad!  You're not allowed to play my game!")
	exit(0)
	
strength = random.randint(0,3)
dexterity = random.randint(0,3)
constitution = random.randint(0,3)
hitpoints = random.randint(5,10) + constitution

print ("Here are your stats:")
sleep(1)
print ("Strength: " + statdescriptor(strength) + " strong")
sleep(1)
print ("Dexterity: " + statdescriptor(dexterity) + " dextrous")
sleep(1)
print ("Constitution: " + statdescriptor(constitution) + " tough")
sleep(1)
print ("Hit Points: " + str(hitpoints))
sleep(1)
goblinkills = 0
spiderkills = 0
xp = 0
turn = 1

print ("\nYou enter the dungeon!")

while hitpoints > 0:
	if turn > 1:
		healme = input("Do you want to heal yourself? (y/n)")
		if healme == 'y':
			healpoints = random.randint(1,2)
			hitpoints = hitpoints + healpoints
			print("You healed yourself!  You now have " + str(hitpoints) + " hit points!")
	
	randmonster = random.randint(1,3)
	if randmonster == 1:
		sleep(1)
		[hitpoints, goblinkills, xp] = fightgoblin(hitpoints, goblinkills, xp)
		print ("You have killed " + str(goblinkills) + " goblins!")
		sleep(1)
	elif randmonster == 2:
		sleep(1)
		[hitpoints, spiderkills, xp] = fightspider(hitpoints, spiderkills, xp)
		print ("You have killed " + str(spiderkills) + " spiders!")
		sleep(1)
	else:
		print ("You wander the dungeon for a while...")
		sleep(1)
	turn = turn + 1
	
print ("Sorry, you died! But you killed " + str(goblinkills) + " goblins!")
sleep(1)
print ("You also killed " + str(spiderkills) + " spiders.")
sleep(1)
print ("You survived " + str(turn) + " encounters!")
print ("\n so there's that...")
