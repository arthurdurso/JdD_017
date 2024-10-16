from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    # Colunas Base
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)

    # Relacionamentos
    produtos = relationship('Produto', back_populates='fornecedor')


class Produto(Base):
    __tablename__ = 'produtos'

    # Colunas Base
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Integer)

    # Coluna Estrangeira
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Relacionamentos
    fornecedor = relationship('Fornecedor', back_populates='produtos')
