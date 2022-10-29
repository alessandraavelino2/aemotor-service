
from helpers.database import db
class Prefeitura(db.Models):
    __tablename__ = "tb_prefeitura"
    id = db.Column(db.Integer, primary_key=True)
    nomePrefeito = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(11), unique=True, nullable=False)
    secretarios = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, nomePrefeito, email, secretarios,telefone):
        self.nomePrefeito = nomePrefeito
        self.email = email
        self.telefone = telefone
        self.secretarios = secretarios
        
        


    def __repr__(self):
        return f'Prefeitura(Prefeito={self.nomePrefeito}, Email={self.email}, Telefone={self.telefone}, Secretários={self.secretarios})'
