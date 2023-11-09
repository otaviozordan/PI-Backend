
from flask import Flask, Response
import json
import sys

# Configura o Flask
app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')


@app.route('/signup', methods=['POST'])
def signup():
    return Response(json.dumps({'login':True}), status=200, mimetype="application/json")

@app.route('/whoami', methods=['GET'])
def whoami():
    resp = {
            'email':'athos@gmail.com', 
            'sensores':{
                'temperatura1':'28C'
            },
            'atuadores':{
                'rele1':{
                    'rotina':'manual',
                    'estado':'ligado',
                },
            }
        }
    return Response(json.dumps(resp), status=200, mimetype="application/json")

#from app.controllers import redirect