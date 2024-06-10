"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'

app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.route('/api/cupcakes', methods=['GET', 'POST'])
def get_cupcakes():
    if request.method == 'GET':
        return jsonify(cupcakes=[c.serialize() for c in Cupcake.query.all()])
    else:
        flavor = request.json['flavor']
        size = request.json['size']
        rating = request.json['rating']
        image = request.json['image']
        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(cupcake)
        db.session.commit()
        response = jsonify(cupcake=cupcake.serialize())
        response.status_code = 201
        return response


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())
