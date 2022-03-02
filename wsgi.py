from flask import Flask
from markupsafe import escape
import logging
import requests


application = Flask(__name__)

def callJiraBack(post_id):
    logging.warning(f'callJira post id = {post_id}')
    header = {"Content-type": "application/json"}
    payload = {"issue": post_id}
    r = requests.post("https://issues.redhat.com/rest/cb-automation/latest/hooks/e95e5bcfcb8a8bed126251d3e110d11bdcc68e0f", data=payload, headers=header)
    logging.warning(f'r = {r}')

@application.route("/")
def hello():
    return "Hello World!"
    logging.warning('hello world called!')

@application.route("/post/<post_id>")
def show_post(post_id):
    logging.warning(f'post id called, id: {post_id}')
    # show the post with the given id, the id is an integer
    
    #This is where we would actually do our API call to the Errata tool to check if status is SHIPPED_LIVE
    #but for proof of concept, we are calling jira back for now to close ticket.
    callJiraBack(post_id)
    return f'Post {post_id}'

if __name__ == "__main__":
    application.run()
