#rock paper sciscoors with the computer
import random
print('....rock ....\n ...paper...\n....sciscors')
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
elif player1 =='rock' and computer =='paper':
	print('player1 WINS')
elif player1 =='sciscors'and computer =='paper':
	print('player1 WINS')
elif player1 =='sciscors' and computer =='rock':
	print('player2 WINS')
elif player1 =='paper' and computer =='sciscors':
	print('computer WINS')
elif player1 =='paper' and computer =='rock':
	print('computer WINS')
elif player1==computer:
	print('ITS a TIE')
else:
	print('something went wrong')
