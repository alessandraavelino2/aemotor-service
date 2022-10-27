
class Prefeitura():

    def __init__(self, nome, email, secretarios,telefone, nomePrefeito):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.secretarios = secretarios
        self.nomePrefeito = nomePrefeito
        


    def __repr__(self):
        return f'Prefeitura(Nome={self.nome}, Email={self.email}, Telefone={self.telefone}, Secretários={self.secretarios}, Prefeito={self.nomePrefeito})'
