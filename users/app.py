# import consul
# consul.register()
import os
from flask import Flask
# import consul

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# consul.register()


import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User


@app.route("/")
def hello():
    return "Hello from Users!"


@app.route("/add")
def add_user():
    name = request.args.get('name')
    username = request.args.get('username')
    date_published = request.args.get('date_published')
    try:
        user = User(
            name=name,
            username=username,
            date_published=date_published
        )
        db.session.add(user)
        db.session.commit()
        return "User added. book id={}".format(user.id)
    except Exception as e:
        return (str(e))


@app.route("/getall")
def get_all():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return (str(e))


@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        user = User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
