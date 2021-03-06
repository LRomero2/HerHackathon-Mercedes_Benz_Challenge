import os
from flask import (
    Flask, flash, render_template,
    request, session, url_for)


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
