from board import Board
def main():
	b = Board()
	b.initialize()
	# print "team 1:"
	# print(b.valid_moves(1))
	# print "team 2:" 
	# print(b.valid_moves(2))
	player = 1
	while(True):
		moves = b.valid_moves(1)
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
			answer = int(raw_input("Where should it move to?"))
		
		chosen = answer - 1
		move = move_dict[chosen]

		b.move(piece[0][0], piece[0][1], move[0], move[1])
		b.print_board()

if __name__ == '__main__':
	main()