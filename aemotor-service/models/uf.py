from helpers.database import db
class Uf(db.Models):
    __tablename__ = "tb_uf"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    sigla = db.Column(db.String(5), nullable=False)
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla


    def __repr__(self):
        return f'Uf(Curso={self.nome}, Matrícula={self.sigla})'
