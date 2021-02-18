from flask import Flask
from routing.home import app as home
from routing.salmaa import app as salmaa
from routing.farhan import app as farhan
from routing.yoas import app as yoas
from routing.deera import app as deera
from routing.eben import app as eben
from routing.azka import app as azka

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(salmaa)
app.register_blueprint(farhan)
app.register_blueprint(yoas)
app.register_blueprint(deera)
app.register_blueprint(eben)
app.register_blueprint(azka)

if __name__ == '__main__':
    app.run()