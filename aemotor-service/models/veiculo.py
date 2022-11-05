from helpers.database import db
class Veiculo(db.Models):
    __tablename__ = "tb_veiculo"

    cidade = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    qtdPassageiros = db.Column(db.String(7), nullable=False)
    tipoVeiculo = db.Column(db.String(50), nullable=False)
    placa = db.Column(db.String(10), nullable=False)
    motoristaParentId = db.Column(db.Integer, db.ForeignKey("tb_motorista.id"))
    
    def __init__(self, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa


    def __repr__(self):
        return f'Veiculo(Cidade={self.cidade}, Qtd. Passageiros={self.qtdPassageiros}, Tipo de Veículo={self.tipoVeiculo}, Placa={self.placa})'
