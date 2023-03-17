from flask import Flask, jsonify, request
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
    drinks = DRINK.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks": output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink = DRINK.query.get_or_404(id)
    return jsonify({"name": drink.name, "description": drink.description})


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = DRINK(name=request.json['name'],
                  description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}


@app.route('/drinks/<id>', methods={'delete'})
def delete_drink(id):
    drink = DRINK.query.get(id)
    db.session.delete(drink)
    db.session.commit()
    return "removed drink"
