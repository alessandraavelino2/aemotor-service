from models.pessoa import Pessoa
from helpers.database import db

class Aluno(Pessoa, db.Models):
    __tablename__ = "tb_aluno"
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), nullable=False)
    instituicaoDeEnsino = db.Column(db.String(60), nullable=False)
    curso = db.Column(db.String(60), nullable=False)
    
    parent_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    parent = db.relationship("Pessoa")

    def __init__(self, curso, matricula, instituicaoDeEnsino, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)
        self.matricula = matricula
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso

    def __repr__(self):
        return f'Aluno(Curso={self.curso}, Matrícula={self.matricula}, Instituição de Ensino={self.instituicaoDeEnsino}, Nome={self.nome}, Nascimento={self.nascimento}, Email={self.email}, Telefone={self.telefone})'
