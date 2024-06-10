"""Flask app for Cupcakes"""
from flask import Flask, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'

app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)