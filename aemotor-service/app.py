# from models.aluno import Aluno
# from models.cidade import Cidade
# from models.instituicaoDeEnsino import InstituicaoDeEnsino
# from models.pessoa import Pessoa
# from models.endereco import Endereco
# from models.funcionario import Funcionario
# from models.prefeitura import Prefeitura
# from models.gestorApp import GestorApp
# from models.instituicaoDeEnsino import InstituicaoDeEnsino
# from models.motorista import Motorista
# from models.passageiro import Passageiro
# from models.prefeito import Prefeito
# from models.rota import Rotagi
# from models.veiculo import Veiculo
# from models.uf import Uf

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from helpers.database import db, migrate

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

# cidade = Cidade("Belém", "BEL")
# prefeitura = Prefeitura("Pref. Mun. de Belém", "belem@mail.com", "Pedro", "0393432", "Renata")
# pessoa = Pessoa("Alessandra", "23/01/2002", "ale123@mail.com", "83996097405")
# endereco = Endereco("dpf", "oasdjo", "askodj", "asofp", "ijfd")
# funcionario = Funcionario(prefeitura, "Acessor")
# aluno = Aluno("João", "19/10/2004", "joao@mail.com", "4985743", "IFPB", "TSI", "9384039284")
# gestorApp = GestorApp("Alessandra A", "admin@mail.com", "8489578379", "23/01/2002")
# instituicaoDeEnsino = InstituicaoDeEnsino(endereco, "343645654", "IFPB" )
# motorista = Motorista("IFPB-GBA, UFPB-GBA, EESAP-GBA", prefeitura, "Motorista")
# passageiro = Passageiro("Belém", "Guarabira", aluno)
# prefeito = Prefeito(prefeitura, "12/10/1992", "prefeita@mail.com", "34834834")
# veiculo = Veiculo("Belém", "44", "Ônibus Escolar", "ABC-123")
# rota = Rota("Guarabira", "40", prefeitura, veiculo, "12:30", "18:00", passageiro )
# uf = Uf("Paraíba", "PB")

# print(aluno)
# print(cidade)
# print(pessoa)
# print(prefeitura)
# print(endereco)
# print(funcionario)
# print(gestorApp)

# print(instituicaoDeEnsino)
# print(motorista)
# print(passageiro)

# print(prefeito)
# print(veiculo)
# print(rota)
# print(uf)

# python -m venv venv
# .\venv\Scripts\Activate.ps1