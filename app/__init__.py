from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from random import randint

# Create the app
app = Flask(__name__)

# ------------------------------------------
# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# ------------------------------------------
# About page - loading a static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# ------------------------------------------
# Random Number Page - passing a value into template
@app.get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template('pages/random.jinja', number=randNum)

# ------------------------------------------
# Number Page - Getting a value from route
#               and passing it into template
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You entered: {num}")
    return render_template('pages/number.jinja', number=num)

# ------------------------------------------
# Form Page - Static page with a form!
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')


# ------------------------------------------
# Handle data posted from the form
@app.post("/processForm")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        name = request.form["name"],
        age = request.form["age"]
        )


# ------------------------------------------
# Handle any missing pages
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")