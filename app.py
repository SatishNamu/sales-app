from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
from models.user import User
from models.course import Course

@app.route('/')


def hello_world():
    rec = db.get_or_404(Course,1)
    return f"HELLO WORLD.! from {rec.username} "

