class InstituicaoDeEnsino():
    def __init__(self, endereco, telefone, nome):
        self.endereco = endereco
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return f'InstituicaoDeEnsino(endereco={self.endereco}, Telefone={self.telefone}, Nome={self.nome})'
