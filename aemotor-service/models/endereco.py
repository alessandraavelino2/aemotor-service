class Endereco:
    def __init__(self, cep, numero, complemento, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro

    def __repr__(self):
        return f'Endereço(CEP={self.cep}, Número={self.numero}, Complemento={self.complemento}, Referência={self.referencia}, Logradouro={self.logradouro})'
