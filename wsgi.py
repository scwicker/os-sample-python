from flask import Flask
from markupsafe import escape
import logging
import requests


application = Flask(__name__)

def callJiraBack(post_id):
    logging.warning(f'callJira post id = {post_id}')
    headers = {"Content-type": "application/json"}
    params = {"issue": post_id}
    r = requests.post("https://issues.redhat.com/rest/cb-automation/latest/hooks/e95e5bcfcb8a8bed126251d3e110d11bdcc68e0f", params=params, headers=headers)
    logging.warning(f'r = {r}')
    logging.warning(f'r = {r.request.url}')
    logging.warning(f'r = {r.request.body}')
    logging.warning(f'r = {r.request.headers}')

@application.route("/")
def hello():
    return "Hello World!"
    logging.warning('hello world called!')

@application.route("/post/", methods=['POST'])
def show_post():
    logging.warning(f'post id called, id: {post_id}')
    # show the post with the given id, the id is an integer
    
    #This is where we would actually do our API call to the Errata tool to check if status is SHIPPED_LIVE
    #but for proof of concept, we are calling jira back for now to close ticket.
    #callJiraBack(post_id)
    
    #return f'Post {post_id}'
    return request.json

if __name__ == "__main__":
    application.run()
