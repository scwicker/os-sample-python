from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

if __name__ == "__main__":
    application.run()
