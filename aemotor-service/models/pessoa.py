class Pessoa():
    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
            return f'Pessoa(Nome={self.nome}, Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'

