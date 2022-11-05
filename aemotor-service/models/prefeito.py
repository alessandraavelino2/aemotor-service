from models.pessoa import Pessoa
from models.prefeitura import Prefeitura
from helpers.database import db

class Prefeito(Pessoa, db.Models):
    __tablename__ = "tb_prefeito"
    __mapper_args__ = {'polymorphic_identity': 'prefeito', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    nomePrefeito = db.Column(db.String(100), nullable=False)

    pessoaParentId = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeituraParentId = db.Column(db.Integer, db.ForeignKey("tb_prefeitura.id"))
    pessoa = db.relationship("Pessoa",foreign_keys=[pessoaParentId])
    
    def __init__(self, prefeitura, nascimento, email, telefone):
        super().__init__(prefeitura, nascimento, email, telefone)
        self.prefeitura = prefeitura
    def __repr__(self):
        return f'Prefeito(Prefeitura={self.prefeitura}, Dt. Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'
