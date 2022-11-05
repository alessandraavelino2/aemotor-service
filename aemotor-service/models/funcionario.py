from models.pessoa import Pessoa
from helpers.database import db

class Funcionario(Pessoa, db.Models):
    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario', 'concrete': True}
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(40), nullable=False)
    cargo = db.Column(db.String(6), nullable=False)

    pessoaParentId = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    motoristaChild = db.relationship("Motorista", uselist=False)
    prefeituraId = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
    pessoa = db.relationship("Pessoa",foreign_keys=[pessoaParentId])

    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo


    def __repr__(self):
        return f'Funcionario(Prefeitura={self.prefeitura}, Cargo={self.cargo})'
