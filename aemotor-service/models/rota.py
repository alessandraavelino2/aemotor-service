
from helpers.database import db
class Rota(db.Models):
    __tablename__ = "tb_rota"
    id = db.Column(db.Integer, primary_key=True)
    cidadeDestino = db.Column(db.String(100), nullable=False)
    qtdalunos = db.Column(db.String(7), nullable=False)
    prefeitura = db.Column(db.String(100), nullable=False)
    veiculo = db.Column(db.String(50), nullable=False)
    horaSaida = db.Column(db.datetime(), nullable=False)
    horaChegada = db.Column(db.datetime(), nullable=False)
    passageiro = db.Column(db.String(100), nullable=False)

    prefeituraChild = db.relationship("Prefeitura", uselist=False)
    instituicaoDeEnsino = db.relationship('InstituicaoDeEnsino', backref='InstituicaoDeEnsino', lazy=True)
    alunos = db.relationship('Aluno', backref='Aluno', lazy=True)
    

    def __init__(self, cidadeDestino, qtdAlunos, prefeitura, veiculo, horaSaida, horaChegada, passageiro):
        self.cidadeDestino = cidadeDestino
        self.qtdAlunos = qtdAlunos
        self.prefeitura = prefeitura
        self.veiculo = veiculo
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada
        self.passageiro = passageiro

    def __repr__(self):
        return f'Rota(Destino={self.cidadeDestino}, Qtd. Alunos={self.qtdAlunos}, Prefeitura={self.prefeitura}, Veículo={self.veiculo}, Hr. Saída={self.horaSaida}, Hr. Chegada={self.horaChegada}, Passageiros={self.passageiro})'
