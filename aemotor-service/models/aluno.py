from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, curso, matricula, instituicaoDeEnsino, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)
        self.curso = curso
        self.matricula = matricula
        self.instituicaoDeEnsino = instituicaoDeEnsino

    def __repr__(self):
        return f'Aluno(Curso={self.curso}, Matrícula={self.matricula}, Instituição de Ensino={self.instituicaoDeEnsino}, Nome={self.nome}, Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'
