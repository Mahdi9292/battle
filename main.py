from classees.game import person, bcolors
from classees.magic import Spell

# Create Black Magic
fire = Spell("Fire", 40, 90, "black")
thunder = Spell("Thunder", 80, 180, "black")
blizzard = Spell("Blizzard", 120, 270, "black")
meteor = Spell("Meteor", 160, 360, "black")
quake = Spell("Quake", 200, 450, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "whit")
cura = Spell("Cura", 18, 200, "whit")

# player_magic = [{"name": "Fire", "cost": 40, "dmg": 90},
# 		 {"name": "Thunder", "cost": 80, "dmg": 180},
# 		 {"name": "Blizzard", "cost": 120, "dmg": 270}]

# Instantiate People
player = person(500, 200, 60, 35, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = person(1200, 70, 30, 20, [])

running = True
i = 0

print(bcolors.FAIL, bcolors.BOLD, "AN ENEMY ATTACKS!", bcolors.ENDC)

while running:
	print("==========================")
	player.choose_action()
	choice = input("Choose Action:")
	index = int(choice) - 1

	if index == 0:
		p_dmg = player.generate_damage()  # p_dmg ==> player dmg
		enemy.take_damage(p_dmg)
		print("Your attack damage was:", p_dmg, "points of damage")
	elif index == 1:
		player.choose_magic()
		magic_choice = int(input("NOW	!!! Choose Magic Sir:")) - 1

		# magic_dmg = player.generate_spell_damage(magic_choice)
		# spell = player.get_spell_name(magic_choice)
		# cost = player.get_spell_mp_cost(magic_choice)

		spell = player.magic[magic_choice]
		magic_dmg = spell.generate_damage()

		current_mp = player.get_mp()

		if spell.cost > current_mp:
			print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
			continue  # The continue statement in Python returns the control to the beginning of the while loop.
		player.reduce_mp(spell.cost)
		enemy.take_damage(magic_dmg)
		print(bcolors.OKBLUE + "\n" + spell.name + str(magic_dmg), "points of damage" + bcolors.ENDC)

	enemy_choice = 1

	e_dmg = enemy.generate_damage()  # e_dmg ==> enemy dmg
	player.take_damage(e_dmg)
	print("Enemy's attack damage was", e_dmg, "points of damage")

	print("------------------------------------------")
	print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
	print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
	print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
	if enemy.get_hp() == 0:
		print(bcolors.OKGREEN + "You Win" + bcolors.BOLD, bcolors.ENDC)
		running = False
	elif player.get_hp() == 0:
		print(bcolors.FAIL + "You Loose" + bcolors.BOLD, bcolors.ENDC)
		running = False
