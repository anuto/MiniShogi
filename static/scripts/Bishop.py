from Piece import Piece

class Bishop(Piece):
	def __init__(self, team):
		self.name = 'Bishop'
		self.team = team
		Piece.__init__(self, team, ["DragonHorse"])

	def get_info(self, x, y, board, moves):	
		empty = self.is_empty(x, y, board)
		if empty:
			return False
		elif self.on_same_team(x, y, board):
			return None
		else:
			return True

	def get_moves(self, x, y, board):
		moves = []
		
		for i in range(1, 6):
			x_coord = x - i
			y_coord = y - i

			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None:
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						break

		for i in range(1, 6):
			x_coord = x + i
			y_coord = y + i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None:
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						break

		for i in range(1, 6):
			x_coord = x + i
			y_coord = y - i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None:
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						break

		for i in range(1, 6):
			x_coord = x - i
			y_coord = y + i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None:
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						break

		if self.promoted:
			for x_coord in range(-1, 2):
				for y_coord in range(-1, 2):
					if self.check(x_coord + x, y_coord + y, board):
						moves += [(x_coord + x, y_coord + y)]

		return moves
