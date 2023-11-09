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
	code:str
	adresses:List['Address']=Relationship()
	accounts:List['Account']=Relationship()
	quotas:List['Quota']=Relationship()

class Address(SQLModel, table=True):
	"""docstring for Address"""
	id: Optional[int] = Field(default=None, primary_key=True)
	street:str
	number:str 
	city:str
	state:str
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





def create_shareholder(
	name:str, 
	email: str, 
	cpf: str, 
	birth: str, 
	telephone: str, 
	cell: str, 
	
	):
	with Session(engine) as session:
		session.add(User(name=name, email=email, cpf=cpf, birth=birth, telephone=telephone, cell=cell, status = "ativo" , code = "123"))
		session.commit()



def update_shareholder(
	name:str, 
	email: str, 
	cpf: str, 
	birth: str, 
	telephone: str, 
	cell: str,
	street:str,
	number:str,
	city:str,
	state:str,
	cep:str,
	id,
	
	):
	with Session(engine) as session:
		
		user = session.get(User, id)
		if name:
			user.name = name
		if email:
			user.email = email
		if cpf:
			user.cpf = cpf
		if birth:
			user.birth = birth
		if telephone:
			user.telephone = telephone
		if cell:
			user.cell = cell
		
		address = session.get(Address, user.id)
		if street:
			address.street=street
		if number:
			address.number=number
		if cep:
			address.cep=cep
		if city:
			address.city=city
		if state:
			address.state=state


		session.commit()
		


def list_users_shareholder(filters:str, offset:str, per_page:str ):
	with Session(engine) as session:
		query = select(User)
		if filters:
			query = query.where( or_(User.name.contains(filters),User.cpf.contains(filters)) )
		
		query = query.offset(offset).limit(per_page)

				
		data = session.exec(query).all()
		return data

def view_user_shareholder(id:str):
	with Session(engine) as session:
		query = select(User,Address).join(Address)
		query = query.where(User.id == id )

		data = session.exec(query).first()
		print(data)
		return data




"""
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from flask import Flask, render_template, request

# Defina o modelo SQLModel
class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    content: str

# Crie uma instância do mecanismo SQLAlchemy e uma sessão
engine = sa_create_engine('sqlite:///example.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)  # Obtenha o número da página da consulta de URL
    per_page = 5  # Número de itens por página
    offset = (page - 1) * per_page

    with Session(engine) as session:
        stmt = select(Post).offset(offset).limit(per_page)
        posts = session.exec(stmt).all()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

"""





"""

def read_norm_list(description:str=None , tags:str=None, page:str = None):
	with Session(engine) as session:	
		query= select(
			Norm_iten_sub,
			Norm_iten.title,
			Norm_iten.iten,
			).join(Norm_iten)

		if description:
			query = query.where( Norm_iten_sub.description.contains(description))
		if tags and tags != []:
			
			query = query.where( or_(Norm_iten_sub.tag == x for x in tags))
		
		if page:
			index = 10
			query = query.offset(page).limit(index)

		else:
			index = 10
			query = query.limit(index)

			

		data = session.exec(query).all()
"""












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