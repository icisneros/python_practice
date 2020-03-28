import random
import matplotlib.pyplot as plt
import numpy as np


def printHeader():
	print "\n\n######################################################################\n\n"
	print "                    Monty Hall Problem Simulator                      "
	print "\n\n######################################################################\n\n"


def contestant(max_num):
	""" Choose a door by returning a random number between 0 and the length
	    of the 'doors' list
	"""
	return random.randint(0, max_num - 1)


def shuffle_doors(doors):
	""" Returns the index in the shuffled doors list of the winning door (index of the item "car")
	"""

	new_doors = doors

	random.shuffle(new_doors)

	return new_doors.index("car")


def monty(max_num, win_door, cont_choice):
	""" Returns an index that is not the winning door or the door that the contestant chose.
	    Assumes that there is only one winning door.
	"""

	doors_indices = range(0,max_num)  # represent the allowable door choices in terms indices

	if win_door in doors_indices:
		doors_indices.remove(win_door)
	if cont_choice in doors_indices:
		doors_indices.remove(cont_choice)

	return random.choice(doors_indices)


def perform_switch(max_num, cont_choice, monty_choice):
	doors_indices = range(0,max_num)  # represent the allowable door choices in terms indices

	if cont_choice in doors_indices:
		doors_indices.remove(cont_choice)
	if monty_choice in doors_indices:
		doors_indices.remove(monty_choice)

	return random.choice(doors_indices)



if __name__ == '__main__':
	""" Monty hall problem simulator, in order to visualize the difference in win percentage
	    between switching choice and keeping choice -- because it is a very counterintuitive
	    conclusion x(
	"""

	printHeader()


	while True:
	    try:
	        max_games = int(raw_input("Please enter the number of games to simulate: "))
	    except ValueError:
	        print "Sorry, I didn't understand that."
	        continue
	    else:
	        break
	

	# Initialize counters
	games_played = 0
	switched_games_won = 0
	stayed_games_won = 0

	# The following are lists of floats
	switch_percent = [] # percentage wins by switching
	stay_percent = []  # percentage wins by staying

	# Initialize doors
	doors = ["car", "goat", "goat"]
	how_many_doors = len(doors)


	while games_played < max_games:
		
		games_played += 1

		cont_choice = contestant(how_many_doors)

		win_door = shuffle_doors(doors)

		monty_choice = monty(how_many_doors, win_door, cont_choice)

		# case where contestant stays
		if cont_choice == win_door:
			stayed_games_won += 1
		stay_percent.append(stayed_games_won/float(games_played))

		# case where contestant switches
		switched_choice = perform_switch(how_many_doors, cont_choice, monty_choice)
		if switched_choice == win_door:
			switched_games_won += 1
		switch_percent.append(switched_games_won/float(games_played))


	# Print some information
	print "\n\n"
	print "Number of doors: ", str(len(doors))
	print "Total games played: ", str(games_played)
	print "\n"
	print "Number of times won by staying with door choice: ", str(stayed_games_won)
	print "Stayed percentage won: ", str(stay_percent[max_games - 1])
	print "\n"
	print "Number of times won by switching door choice: ", str(switched_games_won)
	print "Switched percentage won: ", str(switch_percent[max_games - 1])


	# plot the stuff - matplotlib requires information be in the form of numpy arrays
	games_list = range(0, max_games)
	games_array = np.array(games_list)

	stay_percent_array = np.array(stay_percent)
	switch_percent_array = np.array(switch_percent)


	# actually plot
	fig = plt.figure()
	ax = plt.subplot(111)

	ax.plot(games_array, stay_percent_array, label='Stay Win Percentage')
	ax.plot(games_array, switch_percent_array, label='Switch Win Percentage')

	ax.legend()

	plt.show()


