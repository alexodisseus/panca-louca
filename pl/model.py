from typing import Optional, List
from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy import func

db = SQLModel()

def configure(app):
    app.db = db



class Person(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	password:str
	kkbkjbkjbkjbkjb
	todos:List['Todo']=Relationship()



class Todo(SQLModel, table=True):
	"""docstring for Todo"""
	id: Optional[int] = Field(default=None, primary_key=True)
	title: str
	status: str = "todo"
	person_id: int = Field(foreign_key='person.id')
	




engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)