import random
#using dictionary
a={1:'rock',2:'paper',3:'scissor'}
while True:
	b=input("enter your choice rock/paper/scissor:")
	#to generate random choice
	c=a[random.randint(1,3)]
	#printing the choices
	print("you chose:",b,"computer chose:",c)
	#comparing the conditions
	if(b==c):
		print("draw")
	elif((b=='rock') and (c=='paper')):
		print("u lose")
	elif((b=='rock') and (c=='scissor')):
		print("u win")
	elif((b=='paper') and (c=='rock')):
		print("u win")
	elif((b=='paper') and (c=='scissor')):
		print("u lose")
	elif((b=='scissor') and (c=='rock')):
		print("u lose")
	elif((b=='scissor') and (c=='paper')):
		print("u win")
	else:
		print("invalid key")
		break