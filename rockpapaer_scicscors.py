#rock paper sciscoors with the computer
import random
player_wins = 0
computer_wins = 0

while player_wins < 2 and compurter_wins < 2:
	
	
	print('....rock ....\n ...paper...\n....sciscors')
	print(f"player score :{player_wins} \n computer score :{computer_wins}")
	player1 = input('player1,enter your choice:\n').lower()
	for i in range(50):
		print( '*********')
	rand = random.randint(0,2)
	if rand = 0:
		computer = "rock"
	elif rand = 1:
		computer = "paper"
	else computer = "sciscors"
	print(f"computer plays{computer}")

	if player1 == 'rock' and computer =='sciscors':
		print('computer WINS')
		computer_wins +=1
	elif player1 =='rock' and computer =='paper':
		print('player1 WINS')
		player_wins += 1
	elif player1 =='sciscors'and computer =='paper':
		print('player1 WINS')
		player_wins += 1
	elif player1 =='sciscors' and computer =='rock':
		print('player2 WINS')
		player_wins += 1
	elif player1 =='paper' and computer =='sciscors':
		print('COMPUTER WINS')
		computer_wins +=1
	elif player1 =='paper' and computer =='rock':
		print('computer WINS')
		computer_wins +=1
	elif player1==computer:
		print('ITS a TIE')
	else:
		print('something went wrong')
