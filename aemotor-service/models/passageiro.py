from models.aluno import Aluno

class Passageiro(Aluno):

    def __init__(self, cidadeOrigem, cidadeDestino, aluno):
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
        self.aluno = aluno
        
    def __repr__(self):
        return f'Passageiro(Origem={self.cidadeOrigem}, Destino={self.cidadeDestino}, Aluno={self.aluno})'
