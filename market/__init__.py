from flask import Flask
from flask_sqlalchemy import SQLAlchemy #za koriscenje mysqlite(db) u flasku i Pajtonu
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Vukoje/Desktop/balša/VS Code/Pajton_projekat/market/instance/market.db'
app.config['SECRET_KEY'] = 'b55af7bc21de6ac108ff731c'  # za sigurnosni layer, prilikom popunjavanja formi

db = SQLAlchemy(app)
bcrypt = Bcrypt(app) # instanca bkripta koji nam sluzi da lozinke cuvamo enkriptovano
login_manager = LoginManager(app)
login_manager.login_view = "login_page" # govori login menadzeru gde da nas login requiered odvede
login_manager.login_message_category = "info" # prikazace poruku da moramo da se logujemo u plavoj boji



