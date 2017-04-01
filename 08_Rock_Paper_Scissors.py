#08 Rock Paper Scissors

exit = "No"

while exit == "No" or exit == "no":
	player_1 = raw_input("Player 1, choose: Rock, Paper, or Scissors ")

	print("You have chosen " + player_1)

	player_2 = raw_input("Player 2, choose: Rock, Paper, or Scissors ")

	print("You have chosen " + player_2)

	#compare data 

	while True:
		if player_1 == "Rock" and player_2 == "Scissors": 
			print "Player 1 Wins!"
			break
		elif player_1 == "Scissors" and player_2 == "Paper":  
			print "Player 1 Wins!"
			break
		elif player_1 == "Paper" and player_2 == "Rock":  
			print "Player 1 Wins!"
			break
		elif player_2 == "Rock" and player_1 == "Scissors": 
			print "Player 2 Wins!"
			break
		elif player_2 == "Scissors" and player_1 == "Paper":  
			print "Player 2 Wins!"
			break
		elif player_2 == "Paper" and player_1 == "Rock":  
			print "Player 2 Wins!"
			break
		elif player_1 == player_2:
			print "It's a tie!"
			break
		else:
			print "Invaild input"
			break


	exit = raw_input("Would you like to quit the game? ")


