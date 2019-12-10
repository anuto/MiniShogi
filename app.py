from flask import Flask, Blueprint, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
 	app.run()