class Uf():
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla


    def __repr__(self):
        return f'Uf(Curso={self.nome}, Matrícula={self.sigla})'
