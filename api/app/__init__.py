
from flask import Flask, Response
import pymongo, json, sys
import sys

from app.mensagens import erro_msg, normal_msg

# Configura o Flask
app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')

# Configura o MongoDB
try:   
    mongoClient = pymongo.MongoClient(app.config['MONGO_URI'])
    mongoDB = mongoClient["PI"]
    normal_msg('Iniciando conexao', mongoDB)
    normal_msg('Banco conectado:', mongoDB.list_collection_names())
   
except Exception as e:
    erro_msg("Ao conectar no Mongo DB", e)
    sys.exit(1)

from app.controllers import redirect