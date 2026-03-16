from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        username = request.form["username"]
        name = request.form["name"]
        title = request.form["title"]
        skills = request.form["skills"]
        projects = request.form["projects"]
        email = request.form["email"]

        db = get_db()

        db.execute(
            "INSERT INTO users (username,name,title,skills,projects,email) VALUES (?,?,?,?,?,?)",
            (username, name, title, skills, projects, email),
        )

        db.commit()

        return redirect("/" + username)

    return render_template("create.html")


@app.route("/<username>")
def portfolio(username):

    db = get_db()

    user = db.execute(
        "SELECT * FROM users WHERE username=?",
        (username,),
    ).fetchone()

    if user:
        return render_template("portfolio.html", user=user)

    return "User not found"


app.run(debug=True)
