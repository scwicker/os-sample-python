from flask import Flask
from markupsafe import escape
import logging
import requests


application = Flask(__name__)

def callJiraBack(post_id):
    logging.warning('callJira post id =', post_id)
    headers = {'Content-type': 'application/json'}
    payload = {'issues': post_id}
    r = requests.post("https://issues.redhat.com/rest/cb-automation/latest/hooks/e95e5bcfcb8a8bed126251d3e110d11bdcc68e0f", data=payload, headers=headers)

@application.route("/")
def hello():
    return "Hello World!"
    logging.warning('hello world called!')

@application.route("/post/<post_id>")
def show_post(post_id):
    logging.warning('post id called!')
    # show the post with the given id, the id is an integer
    callJiraBack(post_id)
    return f'Post {post_id}'

if __name__ == "__main__":
    application.run()
