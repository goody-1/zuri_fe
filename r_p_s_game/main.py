import random

choice_list = ['R', 'P', 'S']
choice_words = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

# word_zip = zip(choice_list, choice_words)
# print(list(word_zip))

print("""This is a simple 'Rock-Paper-Scissors' game
Rules:
	-Rock beats Scissors
	-Paper beats Rock
	-Scissors beats Paper

-> You make a choice by typing a letter amongst r, p and s, signifying your choice of either rock, paper or scissors respectively.

-> You will be playing with the computer, named 'CPU', while you are named 'Player'.

-> The game repeats if it's a tie.

""")

def check_winner(player_choice, cpu_choice):
	"""This function checks who the winner is or if there is tie"""
	if player_choice == 'S' and cpu_choice == 'P':
		winner = "Player"
		tie = False
	elif cpu_choice == 'S' and player_choice == 'P':
		winner = "CPU"
		tie = False
	elif player_choice < cpu_choice:	# P is less than R and R is less than S, this makes it easier
					# only edge case is  S and P as the rule says S beats P, otherwise we can use their ascii code to arrange them...
		winner = "Player"
		tie = False
	elif player_choice > cpu_choice:
		winner = 'CPU'
		tie = False
	else:
		tie = True; winner = ""
		print("There is a tie")
		print("=====Game restarts=====\n")

	return winner, tie


tie = True

while tie:
	cpu_choice = random.choice(choice_list)
	player_choice = input("Enter your choice: ").upper()

	while player_choice not in choice_list:
		print('You entered an invalid choice! Please enter your choice again\n')
		player_choice = input("Enter your choice: ").upper()

	print("Player ({}): CPU ({})".format(choice_words[player_choice], choice_words[cpu_choice]))

	winner, tie = check_winner(player_choice, cpu_choice)

if winner:
	print("\n\t***{} won!!***".format(winner))
	print("\nGame Over")

