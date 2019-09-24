from flask import Blueprint, render_template

toto = Blueprint(
    "toto", __name__, template_folder="/templates", static_folder="/static"
)


@toto.route("/")
def index():
    from datetime import datetime

    d0 = datetime(2019, 9, 23)
    d1 = datetime.now()
    delta = d1 - d0
    return render_template("toto/index.html", smokedate=delta)
