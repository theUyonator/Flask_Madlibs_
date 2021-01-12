from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "MADLIBS"
debug = DebugToolbarExtension(app)

@app.route("/")
def prompt():
    """This function uses the prompts provided to render the madlib_form.html doc"""
    prompts = story.prompts
    return render_template("madlib_form.html", prompts = prompts)

@app.route("/madlib_story")
def madlib_story():
    """This function renders the information entered in the madlib_form.html into a story in madlib_story.html"""
    text = story.generate(request.args)

    return render_template("madlib_story.html", text = text)