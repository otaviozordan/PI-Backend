from app import mongoDB
from models.gerarIds import gerar_id_8_caracteres

class Gateway():
    def __init__(self, nome, descricao):
        self.nome = nome
        self.id = gerar_id_8_caracteres()
        self.descricao = descricao

    def save(self, id_sala):
        novo_gateway = {
            "nome": self.nome,
            "descricao": self.descricao,
            "id":self.id
        }
        filtro = {"sala_id": id_sala}
        novo_campo = {"$set":{'gateway':novo_gateway}}
        x = mongoDB.Salas.update_one(filtro, novo_campo)
        if x.modified_count:
            return 0
        return 1

class Atuador():
    def __init__(self, nome, tipo, descricao, automatico, rotina, estado):
        self.id = gerar_id_8_caracteres()
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.automatico = automatico
        self.rotina = rotina
        self.estado = estado

    def save(self, id_sala):
        nome_atuador = {
            'nome':self.nome,
            'tipo':self.tipo,
            'descricao':self.descricao,
            'automatico':self.automatico,
            'rotina':self.rotina,
            'estado':self.estado
        }
        filtro = {"sala_id": id_sala}
        novo_campo = {"$push":{'atuadores':nome_atuador}}
        mongoDB.Salas.update_one(filtro, novo_campo)
        x = mongoDB.Salas.update_one(filtro, novo_campo)
        if x.modified_count:
            return 0
        return 1
    
def carregar_por_id_sensor_e_sala(cls, id_sala, id_sensor):
    filtro = {"sala_id": id_sala, "atuadores.nome": id_sensor}
    atuador_encontrado = mongoDB.Salas.find_one(filtro, {"atuadores.$": 1})

    if atuador_encontrado:
        atuador_info = atuador_encontrado['atuadores'][0]
        atuador = cls(
            nome=atuador_info['nome'],
            tipo=atuador_info['tipo'],
            descricao=atuador_info['descricao'],
            automatico=atuador_info['automatico'],
            rotina=atuador_info['rotina'],
            estado=atuador_info['estado'],
            id=id_sensor
        )
        return atuador
    else:
        return None
    

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
                    "estado":True
                },           
                {
                    "nome":"rele2",
                    "rotina":"manual",
                    "estado":False
                }
            ]
        }