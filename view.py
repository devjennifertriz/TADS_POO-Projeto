from models.Usuario import Usuario, Usuarios
from models.pedido import Pedido, Pedidos
from models.produto import Produto, Produtos
from models.categoria import Categoria, Categorias

class View:
    @staticmethod
    def Usuario_Inserir(nome, email, fone, senha):
        Inserindo = Usuario(0, nome, email, fone, senha)
        Usuarios.Inserir(Inserindo)
    @staticmethod
    def Usuario_Listar():
        return Usuarios.Listar()
    def Usuario_ListarId(id):
        return Usuarios.Listar_id(id)
    @staticmethod
    def Usuario_Atualizar(id, nome, email, fone, senha):
        Atualizando = Usuario(id, nome, email, fone, senha)
        Usuarios.Atualizar(Atualizando)
    @staticmethod
    def Usuario_Excluir(id):
        Excluindo = Usuario(id, "semnome", "sememail", "")
        Usuarios.Excluir(Excluindo)
    @staticmethod
    def Usuario_Admin():
        pass
    def Usuario_Login(email, senha):
        return True
    @staticmethod
    def Pedido_Inserir(enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario):
        Inserindo = Pedido(0, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario)
        Pedidos.Inserir(Inserindo)
    @staticmethod
    def Pedido_Listar():
        return Pedidos.Listar()
    @staticmethod
    def Pedido_Atualizar(id, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario):
        Atualizando = Pedido(id, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario)
        Pedidos.Atualizar(Atualizando)
    @staticmethod
    def Pedido_Excluir(id):
        Excluindo = Pedido(id, "", "", "", "", "", "")
        Pedidos.Excluir(Excluindo)
    @staticmethod
    def Produto_Inserir(nome, valor, categoria):
        Inserindo = Produto(0, nome, valor, categoria)
        Produtos.Inserir(Inserindo)
    @staticmethod
    def Produto_Listar():
        return Produtos.Listar()
    @staticmethod
    def Produto_Atualizar(id, nome, valor, categoria):
        Atualizando = Produto(id, nome, valor, categoria)
        Produtos.Atualizar(Atualizando)
    @staticmethod
    def Produto_Excluir(id):
        Excluindo = Produto(id, "", "", "")
        Produtos.Excluir(Excluindo)
    