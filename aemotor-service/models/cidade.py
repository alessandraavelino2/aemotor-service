class Cidade():
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        
    def __repr__(self):
        return f'Cidade(Nome={self.nome}, Sigla={self.sigla})'
