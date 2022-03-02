from flask import Flask
from markupsafe import escape
import requests


application = Flask(__name__)

def callJiraBack(post_id):
    #headers = {'X-API-TOKEN': 'your_token_here'}
    payload = {'issues': post_id}
    r = requests.post("https://issues.redhat.com/rest/cb-automation/latest/hooks/e95e5bcfcb8a8bed126251d3e110d11bdcc68e0f", data=payload)
    print(r)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/post/<post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    callJiraBack(post_id)
    return f'Post {post_id}'

if __name__ == "__main__":
    application.run()
