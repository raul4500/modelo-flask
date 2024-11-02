class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

# Lista simulada de produtos (substituível por um banco de dados real)
produtos = [
    Produto(1, "Laranja", 10.0),
    Produto(2, "Banana", 20.0),
    Produto(3, "Maçã", 15.0)
]

def obter_produto_por_id(produto_id):
    return next((produto for produto in produtos if produto.id == produto_id), None)
