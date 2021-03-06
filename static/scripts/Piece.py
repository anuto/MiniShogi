class Piece(object):

	def __init__(self, team, promotions = None):
		self.team = team
		self.promoted = None
		self.promotions = promotions
		
	def __repr__(self):
		if self.promoted:
			return (self.promoted[0] + str(self.team))
		else:
			return (self.name[0] + str(self.team))

	def check(piece, x, y, board):
		if x >= 0 and x < 5 and y >= 0 and y < 5:
			current = board[y][x]
			if current == None:
				return True
			return current.team != piece.team
		else:
			return False

	def on_same_team(self, x, y, board):
		if not self.is_empty(x, y, board):
			other = board[y][x]
			other_team = other.team
			return other.team == self.team
		else:
			return False

	def is_empty(self, x, y, board): 
		current = board[y][x]
		return current == None


	def is_valid_square(self, x, y):
		return x >= 0 and x < 5 and y >= 0 and y < 5

	def y_dir(piece):
		if piece.team == 1:
			return 1
		else:
			return -1

	def died(self):
		if self.team == 1:
			self.team = 2
		else:
			self.team = 1

		self.promoted = None


	def promotion_ops(self):
		if self.promotions and not self.promoted:
			return self.promotions
		else:
			return None

	def promote(self, role):
		if not self.promotions:
			raise Exception("piece cannot be promoted: " + str(self))
		if role in self.promotions:
			self.promoted = role
		else:
			raise Exception("Invalid role: " + role)