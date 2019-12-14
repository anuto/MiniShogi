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

@app.route('/')
def index():
	# board_state = b.board_state()
	print ("index: " + str(datetime.now()))
	return render_template('index.html', 
		board=board_state, 
		valid_squares=valid_squares, 
		selected=selected, 
		team_1_placeable=team_1_placeable, 
		team_2_placeable=team_2_placeable
	)

@app.route('/get_valid_moves/<int:pos>')
def valid_moves(pos):

	print("vm1: " + str(datetime.now()))
	print("selected: " + str(selected))
	print("pos: " + str(pos))
	if selected == pos:
		global selected
		selected = None
		global valid_squares
		valid_squares = None
	elif not selected or (valid_squares and pos not in valid_squares):
		global valid_squares
		valid_squares = b.valid_moves_from_html(pos)
		global selected
		# TODO: not strictly speaking true. could be an immobilized piece.
		# but also nonideal - highlighting invalid squares
		selected = pos
	else:
		b.move_from_html(selected, pos)
		global valid_squares
		valid_squares = None
		global board_state
		global team_1_placeable
		global team_2_placeable
		board_state, team_1_placeable, team_2_placeable = b.board_state_for_html()
		global selected
		selected = None
	print ("vm2: " + str(datetime.now()))
	return redirect("/")

if __name__ == "__main__":
	app.run(threaded=True)

