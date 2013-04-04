from flask import Flask, render_template, redirect, request
import model 
from model import session 
app = Flask(__name__)

@app.route("/index")
def index():
	#query all users
	#user_list = model.session.query(model.User).limit(5).all()
	#list all users
	return render_template("user_list.html", users=user_list)

#sign up new user
@app.route("/login", methods ="POST")
def login():
	email = request.form["email"]
	password = request.form["password"]
	return redirect(url_for("index"))

@app.route("/register", methods="POST")
def register():
	email = request.form["email"]
	password = request.form["password"]
	existing_user = session.query(User).filter_by(email=email, password=password)
	if existing_user:
		return redirect(url_for("index"))
	u = User(email=email, password=password)
	session.add(u)
	session.commit()
	return redirect(url_for("index"))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
	app.run(debug = True)