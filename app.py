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
@app.route("/landing_page")
def landing_page():
    """ Navigates to Home page. """
    sites = mongo.db.sites.find()
    return render_template("index.html", sites=sites)


@app.route("/get_sites")
def get_sites():
    """ Finds and returns all site reviews. """
    sites = list(mongo.db.sites.find())
    return render_template("sites.html", sites=sites)


@app.route("/view_review/<site_id>")
def view_review(site_id):
    """ Navigates to display the review of the selected site. """
    site = mongo.db.sites.find_one({"_id": ObjectId(site_id)})
    return render_template("view_review.html", site=site)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Retrieves search word and finds matching sites in database. """
    query = request.form.get("query")
    sites = list(mongo.db.sites.find({"$text": {"$search": query}}))
    return render_template("sites.html", sites=sites)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """ Checks if the username already exists in database. """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        """ Returns flash message if user exists."""
        if existing_user:
            flash("Username unavailable. Please try a different username.")
            return redirect(url_for("register"))

        """ Registers if user does not exist."""
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
        }
        mongo.db.users.insert_one(register)

        """ Puts the new user into session cookie."""
        session["user"] = request.form.get("username").lower()
        flash("Sign up successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks if username exists in database.
    Checks password hash matches.
    Allows access if they both match.
    """
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
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


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    """ Finds and returns reviews added by the session user """
    user_sites = list(mongo.db.sites.find({"created_by": session["user"]}))
    sites = list(mongo.db.sites.find())
    return render_template(
        "profile.html", username=username, user_sites=user_sites, sites=sites)


@app.route("/logout")
def logout():
    """ remove session cookies """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("landing_page"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    Retrieves user input from form.
    Appends the database.
    """
    if request.method == "POST":
        members_only = "on" if request.form.get("members_only") else "off"
        review = {
            "site_name": request.form.get("site_name"),
            "location_name": request.form.get("location_name"),
            "visit_date": request.form.get("visit_date"),
            "site_review": request.form.get("site_review"),
            "members_only": members_only,
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.sites.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_sites"))

    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("add_review.html", locations=locations)


@app.route("/edit_review/<site_id>", methods=["GET", "POST"])
def edit_review(site_id):
    """
    Checks if the session user created the review.
    Also checks if the session user is admin.
    Retrieves current data in database.
    Appends database with new data.
    """
    site = mongo.db.sites.find_one({"_id": ObjectId(site_id)})
    if ((session["user"].lower() == site["created_by"].lower())
            or (session["user"] == "admin")):
        if request.method == "POST":

            members_only = "on" if request.form.get("members_only") else "off"
            submit = {
                "site_name": request.form.get("site_name"),
                "location_name": request.form.get("location_name"),
                "visit_date": request.form.get("visit_date"),
                "site_review": request.form.get("site_review"),
                "members_only": members_only,
                "image_url": request.form.get("image_url"),
                "created_by": session["user"]
            }
            mongo.db.sites.replace_one({"_id": ObjectId(site_id)}, submit)
            flash("Review Successfully Edited")
            return redirect(url_for("get_sites"))

    site = mongo.db.sites.find_one({"_id": ObjectId(site_id)})
    locations = mongo.db.locations.find().sort("location_name", 1)
    return render_template("edit_review.html", site=site, locations=locations)


@app.route("/delete_review/<site_id>")
def delete_review(site_id):
    """
    Checks if the session user created the review.
    Also checks if the session user is admin.
    Allows user to delete reviews they created.
    Allows admin to delete any review.
    Navigates back to all sites.
    """
    site = mongo.db.sites.find_one({"_id": ObjectId(site_id)})
    if ((session["user"].lower() == site["created_by"].lower())
            or (session["user"] == "admin")):
        mongo.db.sites.delete_one({"_id": ObjectId(site_id)})
        flash("Review Deleted")
    return redirect(url_for("get_sites"))


@app.route("/get_locations")
def get_locations():
    """
    Only renders for admin.
    Navigates to display all locations in the database.
    """
    locations = list(mongo.db.locations.find().sort("location_name", 1))
    return render_template("locations.html", locations=locations)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    """
    Only renders for admin.
    Enables admin to add a location to the database.
    """
    if request.method == "POST":
        location = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.insert_one(location)
        flash("New location added")
        return redirect(url_for("get_locations"))

    return render_template("add_location.html")


@app.route("/edit_location/<location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    """
    Only renders for admin.
    Enables admin to append a location in the database.
    Returns to all locations.
    """
    if request.method == "POST":
        submit = {
            "location_name": request.form.get("location_name")
        }
        mongo.db.locations.replace_one({"_id": ObjectId(location_id)}, submit)
        flash("Location Updated")
        return redirect(url_for("get_locations"))

    location = mongo.db.locations.find_one({"_id": ObjectId(location_id)})
    return render_template("edit_location.html", location=location)


@app.route("/delete_location/<location_id>")
def delete_location(location_id):
    """
    Only renders for admin.
    Enables admin to delete a location in the database.
    Returns to all locations.
    """
    if (session["user"] == "admin"):
        mongo.db.locations.delete_one({"_id": ObjectId(location_id)})
        flash("Location deleted")
    return redirect(url_for("get_locations"))


@app.route("/contact")
def contact():
    """ renders contact page """
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    """ 404 error handling """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
