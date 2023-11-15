@app.route('/incluir_dispositivo', methods=['POST'])
def incluir_dispositivo():
    data = request.get_json()

    # Verifica se os campos obrigatórios estão presentes
    if 'id_sala' not in data or 'id_dispositivo' not in data:
        return jsonify({'erro': 'Campos obrigatórios ausentes'}), 400

    #Obtém os valores da sala e do dispositivo
    id_sala = data['id_sala']
    id_dispositivo = data['id_dispositivo']

    sala = {'id_sala': id_sala, 'id_dispositivo': id_dispositivo}
    salas.append(sala)

    # Resposta de sucesso
    return jsonify({'mensagem': 'Dispositivo incluído com sucesso'}), 200