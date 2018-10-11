import random
from time import sleep
from os import system

a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print("-----------")
	print(a[0],'|',a[1],'|',a[2],'|')
	print("-----------")
	print(a[3],'|',a[4],'|',a[5],'|')
	print("-----------")
	print(a[6],'|',a[7],'|',a[8],'|')
def possibilities():
	for 1 in a:
		if(i!='x' and i!='0'):
			1.append(i)
	return 1
pli=True
while True:
	printboard()
	if pl1:
		p=int(input("choose your place"))
		if(p in a):
			p(int("player 1 chose",p))
			a[p-1]='k'
			pl1= not pl1
	else:
		w=compturn()
		print("computer chose",w)
		sleep(3)
		a[int(w)-1]='O'
		pl1= not pl1

	for i in (0,3,6):
		if(a[i]==a[i+1] and a[i]==a[i+2]):
			printboard()
			if(a[i]=='x'):
				print("player 1 wins")
				exit()
			else:
				print("computer wins")
				exit()

		if(a[0]==a[4] and a[0]==a[8]):
			printboard()
			if(a[0]=='X'):
				print("player 1 wins")
				exit()
			else:
				print("computer wins")
				exit()
		elif(a[2]==a[4] and a[2]==a[6]):
			printboard()
			if(a[2]=='X'):
				print("player 1 wins")
				exit()
			else:
				print("computer wins")
				exit()
		t=possibilities()
		if(len(t)==0):
			printboard()
			print("it is a tie...")
			exit()



