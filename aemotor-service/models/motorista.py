from models.funcionario import Funcionario

class Motorista(Funcionario):

    def __init__(self, rotas, prefeitura, cargo):
        super().__init__(prefeitura, cargo)
        self.rotas = rotas


    def __repr__(self):
        return f'Motorista(Rotas a seguir={self.rotas}, Prefeitura={self.prefeitura}, Cargo={self.cargo})'
