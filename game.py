print("player 1 : X" + " " + "player 2 : O")
def game():
	turn = "X"
	count = 0
	player_turn = player1

	for i in range(10) :
		print(board)
		print("It's your turn, " + player_turn + ". Where do you want to put your piece?"
		move = eval(input())

		if board(move) == " ":
			board(move) = turn
			count += 1
		else:
			print("This place is already filled.\nMove to which place?"
			continue

		if count >= 5:
			if board[7] == board[8] == board[9] != " ":
				declare_winner(turn)
               		 	break
            		elif board[4] == board[5] == board[6] != " ":  # across the middle
                		declare_winner(turn)
                		break
         		elif board[1] == board[2] == board[3] != " ":  # across the bottom
              			declare_winner(turn)
               			break
            		elif board[1] == board[4] == board[7] != " ":  # down the left side
                		declare_winner(turn)
                		break
            		elif board[2] == board[5] == board[8] != " ":  # down the middle
                		declare_winner(turn)
                		break
            		elif board[3] == board[6] == board[9] != " ":  # down the right side
                		declare_winner(turn)
                		break
            		elif board[7] == board[5] == board[3] != " ":  # diagonal
                		declare_winner(turn)
                		break
            		elif board[1] == board[5] == board[9] != " ":  # diagonal
                		declare_winner(turn)
                		break
		if count == 9:
			print("\nGame Over.\n")
			print("It's a Tie!")

		if turn == "X":
			turn == "O"
			player_turn = player2
		else:
		 	turn == "X"
			player_turn = player1