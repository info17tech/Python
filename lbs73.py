cnt=0
count=0
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
		print("my score=",cnt,"computer score=",count)
	elif((b=='rock') and (c=='paper')):
		print("u lose")
		count+=1
		print("my score=",cnt,"computer score=",count)
	elif((b=='rock') and (c=='scissor')):
		print("u win")
		cnt+=1
		print("my score=",cnt,"computer score=",count)
	elif((b=='paper') and (c=='rock')):
		print("u win")
		cnt+=1
		print("my score=",cnt,"computer score=",count)
	elif((b=='paper') and (c=='scissor')):
		print("u lose")
		count+=1
		print("my score=",cnt,"computer score=",count)
	elif((b=='scissor') and (c=='rock')):
		print("u lose")
		count+=1
		print("my score=",cnt,"computer score=",count)
	elif((b=='scissor') and (c=='paper')):
		print("u win")
		cnt+=1
		print("my score=",cnt,"computer score=",count)
	else:
		print("invalid key")
		break