#positions of playboard
a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print("-----------")
	print(a[0],'|',a[1],'|',a[2],'|')
	print("-----------")
	print(a[3],'|',a[4],'|',a[5],'|')
	print("-----------")
	print(a[6],'|',a[7],'|',a[8],'|')
#using flag
playeroneturn = True

while True:
	printboard()
	p=int(input("choose your place >>"))
	if(p in a):
		if playeroneturn:
			#p=input("choose your place, Player 1 >>")
			print("player 1 chose:",p)
			a[p-1]='X'
			playeroneturn = not playeroneturn
		else:
			#p=input("choose your place, Player 2 >>")
			print("player 2 chose:",p)
			a[p-1]='O'
			playeroneturn = not playeroneturn

		#to check winning condition
		#row check
		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='X':
					print("player 1 wins")
				else:
					print("player 2 wins")
					exit()
		#coloumn check			
		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				if a[i]=='X':
					print("player 1 wins")
				else:
					print("player 2 wins")
					exit()
		        
			#if it is a tie
			for i in range(1,10):
				if(not a):
					print("list is empty")
					print("draw")
			
			#diagonal check
			if(a[0]==a[4] and a[0]==a[8]):
				print("player 1 wins")
			else:
				print("player 2 wins")
				exit()
			if(a[2]==a[4] and a[2]==a[6])
				print("player 1 wins")
			else:
				print("player 2 wins")
				exit()
			
			if(c not in a):
				print("invalid")
				continue
			else:
				print("draw")
				exit()
