import random
while(True):
	a=input("'r' to roll the dice, 'q' to quit the game")
	if a=='r':
		r=random.randint(1,6)
		print(r)
	else:
		break