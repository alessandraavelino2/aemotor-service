from helpers.database import db

class InstituicaoDeEnsino(db.Models):

    __tablename__ = "tb_instituicaoDeEnsino"

    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    alunoParent = db.Column(db.Integer, db.ForeignKey("tb_aluno.id"))
    enderecoChild = db.relationship("Endereco", uselist=False)
    rotaId = db.Column(db.Integer, db.ForeignKey('tb_rota.id'), nullable=False)

    def __init__(self, endereco, telefone, nome):
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return f'InstituicaoDeEnsino(endereco={self.endereco}, Telefone={self.telefone}, Nome={self.nome})'
