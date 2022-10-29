from helpers.database import db

class Pessoa(db.Models):
    __tablename__ = "tb_pessoa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    child = db.relationship("Aluno", uselist=False)
    child = db.relationship("Funcionario", uselist=False)

    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
            return f'Pessoa(Nome={self.nome}, Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'

