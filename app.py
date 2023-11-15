from flask import Flask, request, jsonify
from pymongo import MongoClient
from routes.cadastro import cadastrar_usuario
from routes.login import fazer_login
from config import get_config
from flask_pymongo import PyMongo

#from FlaskAuth.routes import cadastro_mongo, login_mongo

app = Flask(__name__)

config = get_config('development') 
app.config.from_object(config)

mongo = PyMongo(app)

#app.register_blueprint(cadastro_bp)
#app.register_blueprint(login_bp)
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()
users_collection = db['usuarios']

#--

if __name__ == '__app__':
    app.run(debug=True)

    
    