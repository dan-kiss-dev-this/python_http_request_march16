from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# below we make a sql lite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# orm model below using a class


class DRINK(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    return {"drinks": "drink data"}
