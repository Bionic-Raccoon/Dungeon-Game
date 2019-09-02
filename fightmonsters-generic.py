import random
import time
from time import sleep
import string

#Shopping Function
def shopping(gold=0, arms=0, armors=0):
	wanttoshop = "x"
	while wanttoshop not in ["y","n"]:
		wanttoshop = input("Do you want to buy better arms or armor? (y/n) ")
	if wanttoshop == 'y':
		#Shop
		whattobuy = "0"
		while whattobuy not in ["1", "2"]:
			whattobuy = input("Enter 1 to buy weapons, 2 to buy better armor:")
		if wanttobuy == "1":
			if (gold > 49):
				print ("You buy better weapons!")
				arms = arms + 1
				gold = gold - 50
		if wanttobuy == "2":
			if (gold > 49):
				print ("You buy better armor!")
				armor = armor + 1
				gold = gold - 50
	return [gold, arms, armors]

def statdescriptor(stat):
	""" This is just a function to return 'friendly' names for stats"""
	if stat > 4:
		return "godly"
	elif stat == 4:
		return "super"
	elif stat == 3:
		return "very"
	elif stat == 2:
		return "sort of"
	elif stat == 1:
		return "kind of"
	elif stat == 0:
		return "not very"
	else:
		return "the opposite of"
		
def showstats():
	""" This function prints out the character's stat blocks """
	print ("")
	print ("====================")
	print ("Name: " + name)#4FCAA3
	print ("Strength: " + statdescriptor(strength) + " strong")
	print ("Dexterity: " + statdescriptor(dexterity) + " dextrous")
	print ("Constitution: " + statdescriptor(constitution) + " tough")
	print ("Hit Points: " + str(hitpoints) + " (of " + str(maxhitpoints) + ")")
	print ("Armor Class: " + str(armorclass))
	print ("Gold: " + str(totalgold))
	print ("====================\n")
	sleep(3)

def fightmonster(monster="", 
				monstermaxhp=1, 
				monsterac = 10, 
				monsterxp=0, 
				monsterdamage=1, 
				monsterhitbonus = 0, 
				monsterdamagebonus = 0, 
				hitpoints=0, 
				kills=0, 
				xp=0, 
				gp=0):
	""" This is the main fighting part of the program """
	showstats()
	monsterhp = random.randint(1,monstermaxhp)
	print ("\n" + name + " encounters a " + monster + "!")
	sleep(1)
	print ("It has " + str(monsterhp) + " hit points!")
	print (name + " has " + str(hitpoints) + "  hit points!")
	while monsterhp > 0 and hitpoints > 0:
		attack = "x"
		while attack not in ["y","n"]:
			attack = input("Do you want to attack? (y/n)")
		sleep(1)
		if attack == 'y':
			doubledamage = False
			print (name + " tries and hit the " + monster+ "!")
			sleep(1)
			tohit = random.randint(1,20)
			if  tohit == 20:
				doubledamage = True
				print ("\n***Critical hit!!!***\n")
				sleep(2)
			tohit = tohit + strength + arms
			print (name + " rolls a " + str(tohit) + "!!!!")
			if tohit == 1:
				print("Really!?!  A ONE!!!")
				sleep(2)
			sleep(1)
			if tohit > monsterac:
				print (name + " hits the " + monster + "!")
				sleep(1)
				damage = random.randint(1,12) + strength + arms
				if doubledamage:
					damage = damage * 2
					doubledamage = False
				monsterhp = monsterhp - damage
				if monsterhp < 1:
					print (name + " kills the " + monster + "!")
					sleep(1)
					kills = kills + 1
					xp = xp + monsterxp
					gp = gp + (monsterxp/2)
					print (name + " finds " + str(monsterxp/2) + " gold pieces!")
					break
				else:
					print(name + " hits for " + str(damage) + ", the " + monster + ", it has " + str(monsterhp) + " hit points left")
					sleep(1)
			else:
				print (name + "'s pitiful attempt fails!  " + name + " misses the " + monster + "!")
				sleep(1)
		else:
			# This is if you don't enter 'y' when asked if you want to attack
			print(name + " tries and get away!")
			escape = random.randint(1,10) + dexterity
			if escape > 5:
				print (name + " gets away!")
				return [hitpoints, kills, xp, gp]
			else:
				print("The " + monster + " is too fast, " + name + " can't get away!")
		print ("The " + monster + " tries to smite " + name + "!")
		sleep(1)
		if random.randint(1,20) > armorclass:
			damage = random.randint(1,monsterdamage)
			print ("The " + monster + " hits " + name + " for " + str(damage) + " damage!")
			sleep(1)
			hitpoints = hitpoints - damage
			print (name + " has " + str(hitpoints) + " hit points left! (of " + str(maxhitpoints) + ")")
			sleep(1)
		else:
			print ("The " + monster + " misses " + name + "!")
			sleep(1)
	return [hitpoints, kills, xp, gp]
	
keepplaying = True
while (keepplaying):	
	# The program actually starts here!
	name = input("Welcome to the adventure!\nEnter your new character's name: ")
	print ("Your new characters is named: " + name)
	sleep(1)

	# Easter egg
	if name.lower() == "alfonso pipethin":
		print("Hello Dad!") 
		sleep(1)
		print("You are not allowed to play my game")
		sleep(1)
		print("HEHEHEHEHEHEHE")
		sleep(1)
		exit(0)

	# Determine the character's starting stats
	strength = random.randint(0,3)
	dexterity = random.randint(0,3)
	constitution = random.randint(0,3)
	hitpoints = random.randint(5,10) + constitution
	armorclass = 10 + dexterity
	maxhitpoints = hitpoints
	kills = 0
	xp = 0
	turn = 1
	level = 1
	gold = 0
	totalgold = 0
	arms = 0
	armor = 0

	# Test and debug names
	if name == "Claire":
		password = input("What is the secret number?")
		if password == str(1397):
			strength = 5
			dexterity = 5
			constitution = 5
			hitpoints = 100
			maxhitpoints = 100
		else:
			print("Nice try sucka!  You get a normal character....")
			sleep(2)
			print("On second thought,  your character just got worse! (womp womp)")
			strength = strength - 1
			dexterity = dexterity - 1
			constitution = constitution -1
	elif name.lower() == "trash":
		strength = 0
		dexterity = 0
		constitution = 0
		hitpoints = 1

	showstats()
	
	sleep(1)

	print ("\n" + name + " enters the dungeon!")
		
	while hitpoints > 0:
		if turn == 1:
			print ("This is the 1st turn")
		elif turn == 2:
			print ("This is the 2nd turn")
		elif turn == 3:
			print ("This is the 3rd turn")
		else:
			print ("This is the " + str(turn) + "th turn")	
		if turn > 1 and (turn % 3) == 0:
			############################Healing#################################
			healme = "x"
			while healme not in ['y','n']: 
					healme = input("Do you want to heal " + name +  "? (y/n)")
			if healme == 'y':
				healpoints = random.randint(1,2)
				hitpoints = hitpoints + healpoints
				if hitpoints > maxhitpoints:
					hitpoints = maxhitpoints
				print("You healed " + name +  "!  " + name +  " now has " + str(hitpoints) + " hit points!")#F17474
			else:
				# Player is a jerk, so we'll heal the character anyway!
				print("Why not?!?  What's wrong with you?!?\n")
				sleep(2)
				print( name + " decides you're not the boss and heals anyway!")
				hitpoints = maxhitpoints
				print( name + " now has " + str(hitpoints) + " (of " + str(maxhitpoints) + ")")
				sleep(3)
		print("\n\n" + name +  " has " + str(((level-1)*100) + xp) + " experience points!")
		print("(need 100 for next level)")
		
		randmonster = random.randint(1,11)
		# Low level monsters
		if level < 4:
			if randmonster < 5:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("goblin", 6, 12, 25, 6, -1, -1, hitpoints, kills, xp)
				sleep(1)
			elif randmonster > 4 and randmonster < 7:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("giant spider", 15, 13, 40, 8, 1, 1, hitpoints, kills, xp)
				sleep(1)
			elif randmonster == 7:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("ogre", 20, 14, 50, 12, 3, 3, hitpoints, kills, xp)
				sleep(1)
			elif randmonster ==8:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("hill giant", 40, 15, 90, 16, 5, 5, hitpoints, kills, xp)
				sleep(3)
			else:
				print ("\n" + name + " wanders the dungeon for a while...\n")
				sleep(3)
		# High level monsters
		else:
			if randmonster < 5:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("ogre", 20, 14, 20, 12, 3, 3, hitpoints, kills, xp)
				sleep(1)
			elif randmonster > 4 and randmonster < 7:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("troll", 25, 16, 30, 16, 1, 1, hitpoints, kills, xp)
				sleep(1)
			elif randmonster == 7:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("fire giant", 40, 15, 40, 16, 5, 5, hitpoints, kills, xp)
				sleep(1)
			elif randmonster ==8:
				sleep(1)
				[hitpoints, kills, xp, gold] = fightmonster("Dragon", 60, 18, 90, 18, 8, 8, hitpoints, kills, xp)
				sleep(1)
			else:
				print ("\n" + name + " wanders the dungeon for a while...\n")
				sleep(3)
		totalgold = totalgold + gold
		gold = 0	
			
		print (name + " has killed " + str(kills) + " monsters!")
		turn = turn + 1
		
		if totalgold > 49:
			[totalgold, arms, armor] = shopping(totalgold, arms, armor)
			armorclass = armorclass + armor
			armor = 0
			
		if xp > 99:
			# Level up
			level = level + 1
			print("\n--------------")
			print(name + " gained a level!  " + name +  " is now level " + str(level))
			print("You can increase one of " + name +  "'s abilities!")
			validchoice = False
			# Ensure that the player chooses a thing that exists
			while not validchoice:
				choice = input("Which do you want to increase? (str/dex/con)")
				if choice in ['str','dex','con']:
					validchoice = True
				if choice == "str":
					strength = strength + 1
				elif choice == "dex":
					dexterity = dexterity + 1
				elif choice =="con":
					constitution = constitution + 1
			print ("" + name +  "'s hit points increase!")
			hp = maxhitpoints
			hp = hp + random.randint(1,6) + constitution
			maxhitpoints = hp
			xp = xp - 100
			armorclass = 10 + dexterity
			showstats()
			
	print()
	if kills > 0:
		print ("Sorry, " + name + " died! But " + name +  " killed " + str(kills) + " monsters! " + name +  " survived " + str(turn) + " turns! \n so there's that...")
	else: 
		print (name + " killed 0 monsters. You should be ashamed of yourself.  " + name +  " survived " + str(turn) + " turns! \n so there's that...")
		
	sleep(1)
	keepgoing = "x"
	while keepgoing not in ['y','n']: 
		keepgoing = input("\nDo you want to play again? (y/n)")
	if keepgoing == 'n':
		keepplaying = False
		
print ("\nGoodbye!")
