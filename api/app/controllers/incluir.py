from app import app
from flask import request, redirect, url_for, flash, Response
import json

from models.gatewayEatuadorModel import Gateway, Atuador
from models.gerarIds import gerar_id_8_caracteres
from app.mensagens import *
    
@app.route('/incluir_gateway', methods=['POST'])
def incluir_gateway():
    try:
        response = {}
        body = request.get_json()
        nome = body['nome']
        descricao = body['descricao']
        id_sala = body['id_sala']

    except Exception as e:
        response = {
            'create':False,
            'message':'Parametros invalidos ou ausentes',
            'error':str(e)
        }
        return Response(json.dumps(response), status=400, mimetype="application/json")

    try:        
        gateway = Gateway(
            nome=nome, 
            descricao=descricao
        )
        if not gateway.save(id_sala=id_sala):
            response = {
                'create':False,
                'message':'Esse Id de sala nao existe',
            }
            return Response(json.dumps(response), status=400, mimetype="application/json")
        response = {
            'create':True ,
            'message':f'Gateway vinculado a sala {id_sala} com o id {gateway.id}'
        }
        return Response(json.dumps(response), status=200, mimetype="application/json")
        
    except Exception as e:
        response = {
            'create':False,
            'message':'Erro ao cadastrar Gateway',
            'error':str(e)
        }
        return Response(json.dumps(response), status=500, mimetype="application/json")
    
@app.route('/incluir_atuador', methods=['POST'])
def incluir_atuador():
    try:
        response = {}
        body = request.get_json()
        id_sala = body['sala_id']
        nome = body['nome']
        tipo = body['tipo']
        descricao = body['descricao']
        automatico = body['automatico']
        rotina = body['rotina']
        estado = body['estado']

    except Exception as e:
        response = {
            'create':False,
            'message':'Parametros invalidos ou ausentes',
            'error':str(e)
        }
        return Response(json.dumps(response), status=400, mimetype="application/json")

    try:        
        atuador = Atuador(
            nome=nome,
            tipo=tipo, 
            descricao=descricao, 
            automatico=automatico,
            rotina=rotina,
            estado=estado
        )
        if not atuador.save(id_sala=id_sala):
            response = {
                'create':False,
                'message':'Esse Id de sala nao existe',
            }
            return Response(json.dumps(response), status=400, mimetype="application/json")
        response = {
            'create':True ,
            'message':f'Atuador vinculado a sala {id_sala} com o id {atuador.id}'
        }
        return Response(json.dumps(response), status=200, mimetype="application/json")
        
    except Exception as e:
        response = {
            'create':False,
            'message':'Erro ao cadastrar Atuador',
            'error':str(e)
        }
        return Response(json.dumps(response), status=500, mimetype="application/json")