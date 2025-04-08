class Avaliacao:
    def __init__(self, cliente, nota, comentario):
        self.cliente = cliente
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"{self.cliente} - Nota: {self.nota}/5 - Comentário: {self.comentario}"

class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
        self.avaliacoes = []

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print(f"Estoque insuficiente para vender {quantidade} unidades.")

    def reabastecer(self, quantidade):
        self.estoque += quantidade

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def __str__(self):
        avaliacoes_str = "\n".join(str(avaliacao) for avaliacao in self.avaliacoes)
        return (f"Produto: {self.nome}\n"
                f"Preço: R${self.preco:.2f}\n"
                f"Estoque: {self.estoque}\n"
                f"Categoria: {self.categoria.nome}\n"
                f"Avaliações:\n{avaliacoes_str if avaliacoes_str else 'Nenhuma avaliação.'}")

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def visualizar_estoque(self):
        print(f"Estoque da loja {self.nome}:")
        for produto in self.produtos:
            print(f"{produto.nome}: {produto.estoque} unidades")

    def mostrar_detalhes_produto(self, produto):
        print(produto)


if __name__ == "__main__":

    eletronicos = Categoria("Eletrônicos")
    livros = Categoria("Livros")

    celular = Produto("Tablet", 1500.00, 44, eletronicos)
    livro_python = Produto("Livro de romance", 100.00, 40, livros)

    loja = Loja("Jujuba Store")
    loja.adicionar_produto(celular)
    loja.adicionar_produto(livro_python)

    celular.vender(2)
    livro_python.reabastecer(3)

    avaliacao_celular = Avaliacao("Julia", 4, "Produto top")
    celular.adicionar_avaliacao(avaliacao_celular)

    loja.visualizar_estoque()
    loja.mostrar_detalhes_produto(celular)
