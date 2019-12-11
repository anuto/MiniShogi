from Piece import Piece

class Rook(Piece):
	def __init__(self, team):
		self.name = 'Rook'
		self.team = team		
		Piece.__init__(self, team, ["King Dragon"])

	def get_moves(self, x, y, board):
		moves = []

		seen_enemy = False
		for i in range(1, 6):
			x_coord = x
			y_coord = y + i

			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				# hacky way of indicating we've seen something on our team
				if is_blocked == None or (is_blocked and seen_enemy):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for i in range(1, 6):
			x_coord = x
			y_coord = y - i

			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				# hacky way of indicating we've seen something on our team
				if is_blocked == None or (is_blocked and seen_enemy):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for i in range(1, 6):
			x_coord = x + i
			y_coord = y

			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				# hacky way of indicating we've seen something on our team
				if is_blocked == None or (is_blocked and seen_enemy):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for i in range(1, 6):
			x_coord = x - i
			y_coord = y

			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				# hacky way of indicating we've seen something on our team
				if is_blocked == None or (is_blocked and seen_enemy):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True
		return moves

	def get_info(self, x, y, board, moves):
		empty = self.is_empty(x, y, board)
		if empty:
			return False
		elif self.on_same_team(x, y, board):
			return None
		else:
			return True