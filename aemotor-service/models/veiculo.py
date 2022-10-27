class Veiculo():

    def __init__(self, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa


    def __repr__(self):
        return f'Veiculo(Cidade={self.cidade}, Qtd. Passageiros={self.qtdPassageiros}, Tipo de Veículo={self.tipoVeiculo}, Placa={self.placa})'
