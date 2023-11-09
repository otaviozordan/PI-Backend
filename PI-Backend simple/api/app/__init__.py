
from flask import Flask, Response, request
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

@app.route('/consultar_sala', methods=['POST'])
def consultar_sala():
    try:
        response = {}
        body = request.get_json()
        id_sala = body['id_sala']

    except Exception as e:
        response = {
            'create':False,
            'message':'Parametros invalidos ou ausentes',
            'error':str(e)
        }
        return Response(json.dumps(response), status=400, mimetype="application/json")
    
    resp = {
                'email':'athos@gmail.com', 
                'sensores':[
                    {
                        "nome":"temperatura",
                        "id":"ABCDEFGH",
                        "estado":23
                    },
                    {
                        "nome":"ldr",
                        "id":"ABCDEFGH",
                        "estado":1234
                    }
                ],
                'atuadores':[
                    {
                        "nome":"rele1",
                        "id":"ABCDEFGH",
                        "rotina":"automatico",
                        "parametros":"</28",
                        "estado":True
                    },           
                    {
                        "nome":"rele2",
                        "rotina":"manual",
                        "parametros":">/128",
                        "estado":False
                    }
                ]
            }
    return Response(json.dumps(resp), status=200, mimetype="application/json")
#from app.controllers import redirect