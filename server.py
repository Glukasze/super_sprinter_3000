from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def route_index():
    user_stories = data_handler.user_stories
    headers = data_handler.DATA_HEADER

    return render_template('index.html', user_stories=user_stories, headers=headers)


@app.route("/story", methods=["GET", "POST"])
def route_story():
    if request.method == "POST":
        data_handler.add_story(dict(request.form))
        return redirect(url_for("route_index"))
    return render_template("story.html")


@app.route("/post", methods=["POST"])
def route_post():
    pass


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
