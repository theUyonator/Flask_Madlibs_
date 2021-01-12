"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's are some instance stories to get started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# story2 = Story(["work_place", "job_postion", "action", "connect"],
#                 """So I've been applying to {work_place} for the 
#                     {job_position}. I am hoping to {action} with
#                     {connect} to discuss further."""
#                 )
# story3 = Story(["name", "location", "action"],
#                 """I am going out with {name}, we will be going to {location}
#                     to {action}"""
#                 )

# #A dict is created of {id:story, id:story}

# stories = {s.id: s for s in [story, story2, story3]}
