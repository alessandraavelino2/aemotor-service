
class Rota():

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
