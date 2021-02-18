from flask import Blueprint, render_template

app = Blueprint('azka', __name__)

@app.route('/azka')
def halamanUtama():
    return render_template("marthinuntukazka.html")