from flask import Blueprint, render_template

app = Blueprint('yoas', __name__)

@app.route('/yoas')
def rebahantothemax():
    return render_template("yoasuntukpatrick.html")