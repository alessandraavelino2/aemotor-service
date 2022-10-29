from models.pessoa import Pessoa
from helpers.database import db

class Funcionario(Pessoa, db.Models):
    __tablename__ = "tb_funcionario"
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(40), nullable=False)
    cargo = db.Column(db.String(6), nullable=False)

    parent_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    parent = db.relationship("Pessoa")

    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo


    def __repr__(self):
        return f'Funcionario(Prefeitura={self.prefeitura}, Cargo={self.cargo})'
