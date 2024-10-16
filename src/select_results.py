from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.classes.Usuario import Base, Usuario


engine = create_engine('sqlite:///meubanco.bd')
print("Conexão com SQLite estabelecida com sucesso.")

Base.metadata.create_all(engine)
print("Tabela Criada com SQLite estabelecida.")

Session = sessionmaker(bind=engine)
with Session() as session:
    usuario = session.query(Usuario).filter_by(nome='João').first()
    print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")