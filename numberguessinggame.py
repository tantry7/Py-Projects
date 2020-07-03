from random import randint 
number = randint(1,11)
num = None

while True:
	num = input("enter the number")
	num = int(num)
	
	if num < number:
		print("your too low.guess again \n")
		
	elif num > number:
		print("your guess high.guess again : \n")
		
	else:
		print ("your guess is correct")
		choice = input("do you want to continue(Y/N)").lower()
		if choice == "n":
			print("thanks for playing")
			break
		else :
			number = randint(1,11)
			num = None #here it exits the loop with the value of NUM = none so the game(loop) continues 

