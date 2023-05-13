from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, create_session

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/postgres")
session = Session(bind=engine)

session = create_session(bind=engine)

def add_data(full_name, number_class, index_class):
    session.execute(text(f"INSERT INTO public.student(secondname, firstname, middlename) VALUES ('{full_name}', '{number_class}', '{index_class}')"))
    session.commit()
    session.close()