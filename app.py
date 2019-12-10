from flask import Flask, Blueprint, render_template, request, redirect, url_for
from static.scripts import main
from static.scripts import Board 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
	b = Board.Board()
	b.initialize()
	board_state = b.board_state()
	return render_template('index.html', board=board_state)

if __name__ == "__main__":
 	app.run()