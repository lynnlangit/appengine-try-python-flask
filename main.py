import os
import urllib

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

DEFAULT_STUDENT_NAME = 'TKP Student'
DEFAULT_CLASSROOM_NAME = 'TKP World'

@app.route('/')
def hello():
    name = DEFAULT_STUDENT_NAME
    classroom = DEFAULT_CLASSROOM_NAME
    my_name = "is Samantha"
    my_classroom = "is home"

    the_name = my_name
    the_classroom = my_classroom

    if name == DEFAULT_STUDENT_NAME and classroom == DEFAULT_CLASSROOM_NAME:
        return 'Hello to ' + name + ' from the great big ' + classroom
    elif name == my_name and classroom == my_classroom:
        return 'Hello to ' + the_name + ' from the great big ' + the_classroom


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
