from flask import Blueprint, render_template

app = Blueprint('salmaa', __name__)

@app.route('/salmaa')
def halamanmarthin():
    return render_template("marthinuntuksalma.html")