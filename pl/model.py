from typing import Optional, List
from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy import func

db = SQLModel()

def configure(app):
    app.db = db



class Person(SQLModel, table=True):
	"""docstring for Person  -  tabela para usuarios do sistema"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	password:str
	registration:str
	types:str  # do usuario, master ou comum
	todos:List['Todo']=Relationship()





class Todo(SQLModel, table=True):
	"""
	docstring for Todo   -   tabela para as acoes do sistema,
	adicionar valor
	devolver valor 
	"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	observation: str
	nature:str
	value:str
	date:str
	status:str
	person_id: int = Field(foreign_key='person.id')
	

class User(SQLModel, table=True):
	"""docstring for User  -  tabela para cotistas"""
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	cpf:str
	email:str
	birth:str
	telephone:str
	cell:str
	status:str
	adresses:List['Address']=Relationship()
	accounts:List['Account']=Relationship()
	quotas:List['Quota']=Relationship()

class Address(SQLModel, table=True):
	"""docstring for Address"""
	id: Optional[int] = Field(default=None, primary_key=True)
	street:str
	number:str 
	cep:str
	user_id: int = Field(foreign_key='user.id')


class Account(SQLModel, table=True):
	"""docstring for Account"""
	id: Optional[int] = Field(default=None, primary_key=True)
	bank:str
	agency:str
	number_account:str
	user_id: int = Field(foreign_key='user.id')


class Quota(SQLModel, table=True):
	"""docstring for Quota"""
	id: Optional[int] = Field(default=None, primary_key=True)
	code:str
	date:str
	grouping:str #para agrupar tipo 'z a b' 

	user_id: int = Field(foreign_key='user.id')


engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)





def create_shareholder(values):
	with Session(engine) as session:
		print('vai')
		print(values)

		session.add(User(values))
		session.commit()













"""
Tabelas

Person
Para administração do sistema
Em diferentes níveis de acesso e edição

Id
Nome
Matrícula ou código
Senha
Tipo -> comum ou master


Todo -> tarefas
Serve para listar as ações no sistema 
Id 
Nome
Observação
Natureza -> adição de valor, devolver valor
Valor
Person-> id.person
Data
Status -> ok, pendente, autorizado, apagado





User

Id
Nome
Nascimento 
Telefone
Celular
Status -> ativo, inativo 

Endereço -> externo
Conta -> externo




Cotas
Serve para listar todas as cotas

Id
Código
Data
User -> id.user
Agrupamento - none, tipoa, tipob, tipoz




Regras
Calcular allicotas
Corte
Porcentagem
Data aplicação
"""