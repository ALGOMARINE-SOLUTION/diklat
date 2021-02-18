from flask import Blueprint, render_template

app = Blueprint('home', __name__)

@app.route('/salmaa')
def halamanUtama():
    return render_template("marthinuntuksalma.html")