from helpers.database import db

class Cidade(db.Models):
    __tablename__ = "tb_cidade"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    sigla = db.Column(db.String(6), nullable=False)
    
    parent_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        
    def __repr__(self):
        return f'Cidade(Nome={self.nome}, Sigla={self.sigla})'
