from sqlalchemy.types import String
from helpers.database import db

class Pessoa(db.Models):
    __tablename__ = "tb_pessoa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    alunoChild = db.relationship("Aluno", uselist=False)
    funcionarioChild = db.relationship("Funcionario", uselist=False)
    gestorAppChild = db.relationship("GestorApp", uselist=False)
    prefeitoChild = db.relationship("Prefeito", uselist=False)
    enderecoChild = db.relationship("Endereco", uselist=False)

    # Herança: Superclasse
    tipo_pessoa = db.Column('tipo_pessoa', String(50))
    __mapper_args__ = {'polymorphic_on': tipo_pessoa}
    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
            return f'Pessoa(Nome={self.nome}, Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'

