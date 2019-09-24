from datetime import datetime
from flask import Blueprint, render_template


toto = Blueprint(
    "toto", __name__, template_folder="/templates", static_folder="/static"
)


@toto.route("/")
def index():
    d0 = datetime(year=2019, month=9, day=22, hour=21)
    d1 = datetime.now()
    delta = d1 - d0
    return render_template("toto/index.html", smokedate=delta)
