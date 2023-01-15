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
@app.route("/get_sites")
def get_sites():
    sites = mongo.db.sites.find()
    return render_template("sites.html", sites=sites)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username unavailable. Please try a different username.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign up successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if user exists
        if existing_user:
        # check password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # take the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


# log out function
@app.route("/logout")
def logout():
    # remove session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add review function
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        members_only = "on" if request.form.get("members_only") else "off"
        review = {
            "site_name": request.form.get("site_name"),
            "location_name": request.form.get("location_name"),
            "visit_date": request.form.get("visit_date"),
            "site_review": request.form.get("site_review"),
            "members_only": members_only,
            "created_by": session["user"]
        }
        mongo.db.sites.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_sites"))

    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("add_review.html", locations=locations)


# edit button functionality
@app.route("/edit_review/<site_id>", methods=["GET", "POST"])
def edit_review(site_id):
    if request.method == "POST":
        members_only = "on" if request.form.get("members_only") else "off"
        submit = {
            "site_name": request.form.get("site_name"),
            "location_name": request.form.get("location_name"),
            "visit_date": request.form.get("visit_date"),
            "site_review": request.form.get("site_review"),
            "members_only": members_only,
            "created_by": session["user"]
        }
        mongo.db.sites.replace_one({"_id": ObjectId(site_id)}, submit)
        flash("Review Successfully Edited")

    site = mongo.db.sites.find_one({"_id": ObjectId(site_id)})
    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("edit_review.html", site=site, locations=locations)


# Delete button functionality
@app.route("/delete_review/<site_id>")
def delete_review(site_id):
    mongo.db.sites.delete_one({"_id":ObjectId(site_id)})
    flash("Review Deleted")
    return redirect(url_for("get_sites"))


# Manage Locations
@app.route("/get_locations")
def get_locations():
    locations = list(mongo.db.locations.find().sort("location_name", 1))
    return render_template("locations.html", locations=locations)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
