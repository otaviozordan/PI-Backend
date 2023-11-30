from flask import Blueprint, request, jsonify


@app.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    username = data.get('username')
    senha = data.get('senha')

    if username and senha:
        # Verificar se o usuário e a senha correspondem (sem hash)
        usuario = users_collection.find_one({'username': username, 'senha': senha})
        
        if usuario:
            return jsonify({'mensagem': 'Login feito com sucesso!!!'}), 200

    return jsonify({'mensagem': 'Senha ou Email inválidos'}), 401

