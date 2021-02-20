from flask import Blueprint, render_template

app = Blueprint('farhan', __name__)

@app.route('/farhan')
def februariasik():
    return render_template("index.html")