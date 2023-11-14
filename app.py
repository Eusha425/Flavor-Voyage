import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify


# Configure application
app = Flask(__name__)



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/search")
def search():
    if "user_id" in session and session["user_id"] is not None:
        status = "true"
        return render_template("search.html", status=status)
    else:
        status = "false"
        return render_template("search.html", status=status)

@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        if not request.form.get("username"):
            error_message = 'Username is required.'
            return render_template('register.html', error_message=error_message)

        user_name = request.form.get("username")
        rows = db.execute("SELECT * FROM users WHERE name = ?", user_name)
        if len(rows) != 0:
            error_message = 'Username already exists'
            return render_template('register.html', error_message=error_message)

        if not request.form.get("password") or not request.form.get("confirmation"):
            error_message = 'Must fill in the passwords'
            return render_template('register.html', error_message=error_message)

        if request.form.get("password") != request.form.get("confirmation"):
            error_message = 'Passwords do not match!'
            return render_template('register.html', error_message=error_message)

        # generate a hashed password
        hash_pass = generate_password_hash(
            request.form.get("password"), method="pbkdf2", salt_length=16
        )
        # add the new user
        db.execute(
            "INSERT into users (name, password) values (?,?)", user_name, hash_pass
        )

    else:
        return render_template("register.html")
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():

    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            error_message = 'Username is required.'
            return render_template('login.html', error_message=error_message)

        # Ensure password was submitted
        elif not request.form.get("password"):
            error_message = 'Password is required.'
            return render_template('login.html', error_message=error_message)
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE name = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            error_message = 'Invalid username and/or password'
            return render_template('login.html', error_message=error_message)

        # Remember which user has logged in
        session["user_id"] = rows[0]["userID"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/add_to_favorites", methods=["POST"])
def add_to_favorites():
    if "user_id" in session and session["user_id"] is not None:
        user_id = session["user_id"]
        label = request.form.get("label")
        url = request.form.get("url")

        db.execute("INSERT INTO favorites (label, url, user_id) VALUES (?, ?, ?)", label, url, user_id)

        return jsonify(success=True)
    else:
        return jsonify(success=False, message="User not logged in")

@app.route("/favorites")
def favorites():
    if "user_id" in session and session["user_id"] is not None:
        user_id = session["user_id"]
        favorites = db.execute("SELECT * FROM favorites WHERE user_id = ?", user_id)
        return render_template("favorites.html", favorites=favorites)
    else:
        return redirect("/login")
