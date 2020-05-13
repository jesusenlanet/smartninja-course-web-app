import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    some_text = "Lorem ipsum"
    current_year = datetime.datetime.now().year
    current_second = datetime.datetime.now().second
    cities = ["Dublin"]
    return render_template(
        "index.html",
        some_text=some_text,
        current_year=current_year,
        current_second=current_second,
        cities=cities
    )


@app.route('/about-me')
def about_me():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
