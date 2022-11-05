from models.funcionario import Funcionario
from helpers.database import db

class Motorista(Funcionario, db.Models):

    __tablename__ = "tb_instituicaoDeEnsino"
    __mapper_args__ = {'polymorphic_identity': 'motorista', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(200), nullable=False)
    
    funcionarioParentId = db.Column(db.Integer, db.ForeignKey("tb_funcionario.id"))
    veiculoChild = db.relationship('Veiculo',uselist=False)    
    def __init__(self, rotas, prefeitura, cargo):
        super().__init__(prefeitura, cargo)
        self.rotas = rotas


    def __repr__(self):
        return f'Motorista(Rotas a seguir={self.rotas}, Prefeitura={self.prefeitura}, Cargo={self.cargo})'
