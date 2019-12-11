from Board import Board

def main():
	b = test_initialize()

def test_initialize():
	b = Board()
	b.initialize()

	test_team_one(b)
	test_team_two(b)

def test_team_one(b):
	coords = {
		"rook": (0,0),
		"bishop": (1,0),
		"silver gen": (2,0),
		"gold gen": (3,0),
		"emperor": (4, 0),
		"pawn": (4, 1)
	}
	test_team(b, coords, 1)

def test_team_two(b):
	coords = {
		"rook": (4, 4),
		"bishop": (3, 4),
		"silver gen": (2, 4),
		"gold gen": (1, 4),
		"emperor": (0, 4),
		"pawn": (0, 3)
	}
	test_team(b, coords, 2)

def test_team(b, coords, team):
	tests = {}
	for piece, coord in coords.items():
		name = "init " + piece
		piece_at_coord = b.get_piece_name(coord[0], coord[1])
		test = piece_at_coord[0] + str(team)
		tests[name] = test

	run_tests(tests, "team " + str(team) + " initialization")


def run_tests(tests, test_set_name):
	for name, t in tests.items():
		assert t, "Failed test in " + test_set_name + "\n\ttest: " + name
	print("x passed: " + test_set_name)
	
if __name__ == '__main__':
	main()