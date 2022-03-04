from flask import Flask, render_template
#
app = Flask(__name__)

@app.route('/')
def index():
	user_name = 'Adarsh'
	stuff = "this is <strong>bold</strong> text"
	thislist = ["djf","dkuf"]
	return render_template("index.html",
		 thislist = thislist,
		 user_name = user_name)

@app.route('/user/<name>')
def user(name):
	return render_template("user.html", user_name = name)

# Custon error pages

# Invalid Url
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal server error 
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500