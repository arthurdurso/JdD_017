from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from lib.classes.Models import Base, Fornecedor, Produto

engine = create_engine('sqlite:///meubanco_desafio.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
            Fornecedor(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
            Fornecedor(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
            Fornecedor(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
            Fornecedor(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
        ]

        produtos = [
            Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
            Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
            Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
            Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
            Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]

        session.add_all(fornecedores)
        session.add_all(produtos)
        # session.commit() Não precisa por causa do 'with'

        for fornecedor, total_preco in session.query(Fornecedor.nome, func.sum(Produto.preco).label('total_preco')
                                     ).join(Produto, Fornecedor.id == Produto.fornecedor_id
                                     ).group_by(Fornecedor.nome).all():
            print(f"Fornecedor: {fornecedor}, Preço Total: {total_preco}")

except SQLAlchemyError as e:
    print(f"Erro ao inserir fornecedores: {e}")