from Piece import Piece

class Bishop(Piece):
	def __init__(self, team):
		self.name = 'Bishop'
		self.team = team
		Piece.__init__(self, team, ["Horse Dragon"])

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
		
		seen_enemy = False
		for index in range(5):
			i = index + 1
			x_coord = x - i
			y_coord = y - i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None or (seen_enemy and is_blocked):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for index in range(5):
			i = index + 1
			x_coord = x + i
			y_coord = y + i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None or (seen_enemy and is_blocked):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for index in range(5):
			i = index + 1
			x_coord = x + i
			y_coord = y - i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None or (seen_enemy and is_blocked):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		seen_enemy = False
		for index in range(5):
			i = index + 1
			x_coord = x - i
			y_coord = y + i
			if self.is_valid_square(x_coord, y_coord):
				is_blocked = self.get_info(x_coord, y_coord, board, moves)
				if is_blocked == None or (seen_enemy and is_blocked):
					break
				else:
					moves += [(x_coord, y_coord)]
					if is_blocked:
						seen_enemy = True

		return moves
