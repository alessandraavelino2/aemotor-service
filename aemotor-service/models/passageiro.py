from models.aluno import Aluno
from helpers.database import db

class Passageiro(Aluno, db.Models):
    __tablename__ = "tb_passageiro"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cidadeOrigem = db.Column(db.String(100), nullable=False)
    cidadeDestino = db.Column(db.String(100), nullable=False)
    
    alunoParentId = db.Column(db.Integer, db.ForeignKey('tb_aluno.id'))
    def __init__(self, cidadeOrigem, cidadeDestino, aluno):
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
        self.aluno = aluno
        
    def __repr__(self):
        return f'Passageiro(Origem={self.cidadeOrigem}, Destino={self.cidadeDestino}, Aluno={self.aluno})'
