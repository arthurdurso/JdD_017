from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.classes.Usuario import Base, Usuario


engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão com SQLite estabelecida com sucesso.")

Base.metadata.create_all(engine)
print("Tabela Criada com SQLite estabelecida.")

Session = sessionmaker(bind=engine)
with Session() as session:
    usuario = Usuario(nome='João', idade=28)
    session.add(usuario)
    session.commit()
    print("Usuário inserido com sucesso.")