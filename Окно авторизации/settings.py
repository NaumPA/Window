from sqlalchemy import create_engine, Integer,String, Column
from sqlalchemy.orm import Session, declarative_base


engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/postgres")

session = Session(bind = engine)
base = declarative_base()

class Auth(base):
    __tablename__ = "auth"
    id = Column(Integer, primary_key = True)
    login = Column(String, nullable = False)
    password = Column(String, nullable = False)
    
base.metadata.create_all(engine)
