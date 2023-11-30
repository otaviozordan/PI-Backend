from flask import Blueprint, request, jsonify


@app.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    username = data['username']
    senha = data['senha']
    usuario = users_collection.find_one({'username': username})
    if usuario and check_password_hash(usuario['senha'], senha):
        return jsonify({'mensagem': 'Login feito com sucesso!!!'}), 200
    return jsonify({'mensagem': 'Senha ou Email inválidos'}), 401
