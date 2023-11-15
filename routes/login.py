from flask import Blueprint, request, jsonify

#login_bp = Blueprint('login', __name__)


@login_mongo.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    email = data['email']
    senha = data['senha']
    usuario = users_collection.find_one({'email': email})
    if usuario and check_password_hash(usuario['senha'], senha):
        return jsonify({'mensagem': 'Login feito com sucesso!!!'}), 200
    return jsonify({'mensagem': 'Senha ou Email inválidos'}), 401