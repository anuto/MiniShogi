from Piece import Piece

class Bishop(Piece):
	def __init__(self, team):
		self.name = 'Bishop'
		self.team = team
		Piece.__init__(self, team, ["Horse Dragon"])
	
	def get_moves(self, x, y, board):
		moves = []

		seen_enemy = False
		for i in range(5):
			x_coord = x - i
			y_coord = y - i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if self.is_empty(board, x - col, y):
					same_team = self.on_same_team(board, x - col, y)
					if same_team or seen_enemy:
						break
					else:
						seen_enemy = True

		seen_enemy = False
		for i in range(5):
			x_coord = x + i
			y_coord = y + i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if self.is_empty(board, x - col, y):
					same_team = self.on_same_team(board, x - col, y)
					if same_team or seen_enemy:
						break
					else:
						seen_enemy = True

		seen_enemy = False
		for i in range(5):
			x_coord = x + i
			y_coord = y - i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if self.is_empty(board, x - col, y):
					same_team = self.on_same_team(board, x - col, y)
					if same_team or seen_enemy:
						break
					else:
						seen_enemy = True

		seen_enemy = False
		for i in range(5):
			x_coord = x - i
			y_coord = y + i
			if self.check(x_coord, y_coord, board):
				moves += [(x_coord, y_coord)]
				if self.is_empty(board, x - col, y):
					same_team = self.on_same_team(board, x - col, y)
					if same_team or seen_enemy:
						break
					else:
						seen_enemy = True

		return moves
