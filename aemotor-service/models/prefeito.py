from models.pessoa import Pessoa


class Prefeito(Pessoa):
    def __init__(self, prefeitura, nascimento, email, telefone):
        super().__init__(prefeitura, nascimento, email, telefone)
        self.prefeitura = prefeitura
    def __repr__(self):
        return f'Prefeito(Prefeitura={self.prefeitura}, Dt. Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'
