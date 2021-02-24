from flask import Blueprint, render_template

app = Blueprint('nia', __name__)

@app.route('/nia')
def menujutakterbatas():
    return render_template("patrick.html")