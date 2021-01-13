import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    recipes = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful!")
        return redirect(url_for("index", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # checks hashed password against entered password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username")
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "index", username=session["user"]))
            else:
                # invalid password - doesn't match the DB
                flash("Incorrect Username and/or Password entered! Try again")
                return redirect(url_for("login"))

        else:
            # username doesn't match the DB
            flash("Incorrect Username and/or Password entered! Try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        url = request.form.get("name")
        url.replace(" ", "")
        recipe = {
                    "name":  request.form.get("name"),
                    "origin": request.form.get("origin"),
                    "description": request.form.get("description").split("\n"),
                    "ingredients": request.form.get("ingredients").split("\n"),
                    "method": request.form.get("method").split("\n"),
                    "created_by": session["user"],
                    "url": url
                }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully added")
        return redirect(url_for("index"))

    return render_template("add_recipe.html")


@app.route("/")
@app.route("/my_recipes")
def my_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("my_recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
