print('....rock ....\n ...paper...\n....sciscors')
player1 = input('player1,enter your choice:\n')
for i in range(500):
	print( '*********')
player2 = input('player2,enter your choice :\n')

if player1 == 'rock' and player2 =='sciscors':
	print('player2 WINS')
elif player1 =='rock' and player2 =='paper':
	print('player1 WINS')
elif player1 =='sciscors'and player2 =='paper':
	print('player1 WINS')
elif player1 =='sciscors' and player2 =='rock':
	print('player2 WINS')
elif player1 =='paper' and player2 =='sciscors':
	print('player2 WINS')
elif player1 =='paper' and player2 =='rock':
	print('player2 WINS')
elif player1==player2:
	print('ITS a TIE')
else:
	print('something went wrong')