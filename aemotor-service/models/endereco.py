from helpers.database import db
class Endereco(db.Models):
    __tablename__ = "tb_endereco"
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), nullable=False)
    numero = db.Column(db.String(6), nullable=False)
    complemento = db.Column(db.String(20), nullable=False)
    referencia = db.Column(db.String(150), nullable=False)
    logradouro = db.Column(db.String(150), nullable=False)
    
    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    instituicaoDeEnsino_parent = db.Column(db.Integer, db.ForeignKey("tb_InstituicaoDeEnsino.id"))
    
    def __init__(self, cep, numero, complemento, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro

    def __repr__(self):
        return f'Endereço(CEP={self.cep}, Número={self.numero}, Complemento={self.complemento}, Referência={self.referencia}, Logradouro={self.logradouro})'
