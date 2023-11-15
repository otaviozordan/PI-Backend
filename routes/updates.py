@app.route('/atualizacoes', methods=['POST'])
def receber_atualizacoes():
    data = request.get_json()

    # Certifique-se de que os campos necessários estão presentes no JSON
    if 'gateway_id' not in data or 'atuadores' not in data:
        return jsonify({'error': 'Campos obrigatórios ausentes'}), 400

    #Obtém o ID do gateway
    gateway_id = data['gateway_id']

    #Update no estado do gatewa
    database['gateways'][gateway_id] = data.get('gateway_estado', None)

    #Atualiza o estado dos atuadores
    for atuador in data['atuadores']:
        atuador_id = atuador['atuador_id']
        atuador_estado = atuador['estado']

        # Atualiza o estado do atuador no banco de dados
        database['atuadores'][atuador_id] = atuador_estado

    return jsonify({'message': 'Atualizações recebidas com sucesso'}), 200