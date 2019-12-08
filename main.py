from board import Board
def main():
	b = Board()
	b.initialize()
	play_again = True
	while play_again:
		play_game(b)
		response = ""
		while response != "y" and response != "n":
			response = raw_input("play again [y/n]? ")
		play_again = response == "y"
		b.reset_board()


def play_game(b):
	game_over = False
	player = 1
	while not game_over:
		b.print_board()
		moves = b.valid_moves(player)

		print("Valid moves: ")
		enum_moves = enumerate(moves)
		answer = -1
		piece_dict = {}
		while answer < 1 or answer > len(moves.keys()):
			for index, holding in enum_moves:
				s = "[" + str(index + 1) + "]: "
				piece_dict[index] = holding
				s += str(holding) + " to " + str(moves[holding])
				print(s)
			print "\nPlayer " + str(player) + "'s turn: "
			answer = int(raw_input("Which piece would you like to move? "))
		
		chosen = answer - 1
		piece = piece_dict[chosen]
		options = moves[piece]
		enum_options = enumerate(options)
		answer = -1

		move_dict = {}
		while answer < 1 or answer > len(options):
			for index, holding in enum_options:
				print("[" + str(index + 1) + "]: " + str(holding))
				move_dict[index] = holding
			answer = int(raw_input("Where should it move to? "))
		
		chosen = answer - 1
		move = move_dict[chosen]
		
		dead = type(piece[0]) == str
		if dead:
			b.place(piece, move[0], move[1])
		else:
			b.move(piece[0][0], piece[0][1], move[0], move[1])
		if player == 1:
			player = 2
		else:
			player = 1

		game_over = b.game_over()


	print "game over: player " + str(b.get_winner()) +  " won!"

if __name__ == '__main__':
	main()