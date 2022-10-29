from models.pessoa import Pessoa
from helpers.database import db

class GestorApp(Pessoa, db.Models):
    __tablename__ = "tb_gestorApp"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    def __init__(self, nome, email, telefone, nascimento ):
        super().__init__(nome, email, telefone, nascimento)

    def __repr__(self):
        return f'GestorApp(Nome={self.nome}, Email={self.email}, Telefone={self.telefone}, Nascimento={self.nascimento})'