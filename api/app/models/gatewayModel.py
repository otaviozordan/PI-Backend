class Gateway():
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.atuadores = {}
    
    def atribuir_atuador(self, atuador):
        self.atuadores[atuador.id]