from flask import Flask, Blueprint, render_template, request, redirect, url_for
from static.scripts import main
from static.scripts import Board 
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
b = Board.Board()
b.initialize()
valid_squares = None
board_state, team_1_placeable, team_2_placeable = b.board_state_for_html()
selected = None
dead_selected = None
turn = b.get_player_turn()

@app.route('/')
def index():
	global turn
	turn = b.get_player_turn()
	game_over = b.game_over()
	winner = None
	if game_over:
		winner = b.get_winner()

	return render_template('index.html', 
		board=board_state, 
		valid_squares=valid_squares, 
		selected=selected, 
		team_1_placeable=team_1_placeable, 
		team_2_placeable=team_2_placeable,
		dead_selected=dead_selected,
		turn=turn,
	)

@app.route('/get_valid_moves/<int:pos>')
def valid_moves(pos):

	print("vm1: " + str(datetime.now()))
	if b.is_valid_piece(pos):
		if selected == pos:
			global selected
			selected = None
			global valid_squares
			valid_squares = None
		else:
			global valid_squares
			valid_squares = b.valid_moves_from_html(pos)
			global selected
			selected = pos
	print ("vm2: " + str(datetime.now()))
	return redirect("/")

@app.route('/move_selected_to/<int:pos>')
def move_selected_to(pos):
	if valid_squares and pos in valid_squares:
		if selected != None: # needs to be this, 0 evaluates to False apparently
			promotions = b.move_from_html(selected, pos)
			global valid_squares
			valid_squares = None
			global board_state
			global team_1_placeable
			global team_2_placeable
			board_state, team_1_placeable, team_2_placeable = b.board_state_for_html()
			global selected
			selected = None
		elif dead_selected != None: # place
			b.place_from_html(dead_selected, pos)
			global valid_squares
			valid_squares = None
			global board_state
			global team_1_placeable
			global team_2_placeable
			board_state, team_1_placeable, team_2_placeable = b.board_state_for_html()
			global dead_selected
			dead_selected = None

	return redirect("/")

@app.route('/place_piece/<string:given_id>')
def place_piece(given_id):
	if b.is_valid_dead_piece(given_id):
		info = given_id.split("_")
		team = info[0][1]
		index = info[2]
		global dead_selected
		if dead_selected != None and dead_selected == given_id:
			dead_selected = None
			global valid_squares
			valid_squares = None
		else:
			dead_selected = given_id
			global valid_squares
			valid_squares = b.empty_squares_for_html()
	return redirect("/")

@app.route('/reset')
def reset():
	b.reset_board()
	global valid_squares
	valid_squares = None
	global board_state
	global team_1_placeable
	global team_2_placeable
	board_state, team_1_placeable, team_2_placeable = b.board_state_for_html()
	global selected
	global dead_selected
	selected = None
	dead_selected = None
	return redirect("/")

if __name__ == "__main__":
	app.run(threaded=True)

