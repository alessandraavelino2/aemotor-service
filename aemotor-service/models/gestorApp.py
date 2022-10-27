from models.pessoa import Pessoa


class GestorApp(Pessoa):
    def __init__(self, nome, email, telefone, nascimento ):
        super().__init__(nome, email, telefone, nascimento)

    def __repr__(self):
        return f'GestorApp(Nome={self.nome}, Email={self.email}, Telefone={self.telefone}, Nascimento={self.nascimento})'