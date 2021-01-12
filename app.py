from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "MADLIBS"
debug = DebugToolbarExtension(app)

@app.route("/")
def list_of_stories():
    """This function shows the lists of stories"""
    return render_template("list_of_stories.html", stories = stories.values())

@app.route("/madlib_form")
def madlib_form():
    """This function displays form pertaining to story choosen in the home directory"""
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("madlib_form.html", story_id = story_id, title = story.title, prompts = prompts)

@app.route("/madlib_story")
def madlib_story():
    """This function renders the information entered in the madlib_form.html into a story in madlib_story.html"""
    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template("madlib_story.html", title = story.title, text = text)