def enviar_atualizacoes():
    data = request.get_json()

    if 'atuadores' not in data:
        return jsonify({'error': 'Campo "atuadores" ausente'}), 400

    # Atualiza o estado dos atuadores
    for atuador in data['atuadores']:
        atuador_id = atuador['atuador_id']
        atuador_estado = atuador['estado']

        #update no estado do atuador no banco de dados
        database['atuadores'][atuador_id] = atuador_estado

    return jsonify({'message': 'Atualizações dos atuadores enviadas com sucesso'}), 200