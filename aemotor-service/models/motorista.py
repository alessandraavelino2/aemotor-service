from models.funcionario import Funcionario
from helpers.database import db

class Motorista(Funcionario, db.Models):

    __tablename__ = "tb_instituicaoDeEnsino"
    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(200), nullable=False)
    def __init__(self, rotas, prefeitura, cargo):
        super().__init__(prefeitura, cargo)
        self.rotas = rotas


    def __repr__(self):
        return f'Motorista(Rotas a seguir={self.rotas}, Prefeitura={self.prefeitura}, Cargo={self.cargo})'
