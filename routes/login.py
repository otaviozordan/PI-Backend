from flask import Blueprint, request, jsonify


@app.route('/login', methods=['POST'])
def fazer_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Verificar se o usuário e a senha correspondem (sem hash)
        usuario = users_collection.find_one({'username': username, 'password': password})
        
        if usuario:
            return jsonify({'mensagem': 'Login feito com sucesso!!!'}), 200

    return jsonify({'mensagem': 'Senha ou Email inválidos'}), 401

