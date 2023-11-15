from flask import Flask
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, users_collection
from pymongo import MongoClient

#cadastro_bp = Blueprint('cadastro', __name__)

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    email = data['email']
    senha = generate_password_hash(data['senha'])
    
    if users_collection.find_one({'email': email}):
        return jsonify({'mensagem': 'Usuário já existe'}), 409
    novo_usuario = {'email': email, 'senha': senha}
    users_collection.insert_one(novo_usuario)
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso'}), 201