from models.pessoa import Pessoa


class Funcionario(Pessoa):

    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo


    def __repr__(self):
        return f'Funcionario(Prefeitura={self.prefeitura}, Cargo={self.cargo})'
