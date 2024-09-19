from models.Usuario import Usuario, Usuarios
from models.encomenda import Encomenda, Encomendas
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
    def Encomenda_Inserir(enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario):
        Inserindo = Encomenda(0, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario)
        Encomendas.Inserir(Inserindo)
    @staticmethod
    def Encomenda_Listar():
        return Encomendas.Listar()
    @staticmethod
    def Encomenda_Atualizar(id, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario):
        Atualizando = Encomenda(id, enderecoEntrega, status, valorTotal, qtdProduto, idProduto, idUsuario)
        Encomendas.Atualizar(Atualizando)
    @staticmethod
    def Encomenda_Excluir(id):
        Excluindo = Encomenda(id, "", "", "", "", "", "")
        Encomendas.Excluir(Excluindo)
    @staticmethod
    def Produto_Inserir(nome, valor, categoria):
        Inserindo = Produto(0, nome, valor, categoria)
        Produtos.Inserir(Inserindo)
    @staticmethod
    def Produto_Listar():
        return Produtos.Listar()
    @staticmethod
    def Produto_ListarId(id):
        return Produtos.Listar_id(id)
    @staticmethod
    def Produto_Atualizar(id, nome, valor, categoria):
        Atualizando = Produto(id, nome, valor, categoria)
        Produtos.Atualizar(Atualizando)
    @staticmethod
    def Produto_Excluir(id):
        Excluindo = Produto(id, "", "", "")
        Produtos.Excluir(Excluindo)
    def Categoria_Inserir(nome, descricao):
        Inserindo = Categoria(0, nome, descricao)
        Categorias.Inserir(Inserindo)
    @staticmethod
    def Categoria_Listar():
        return Categorias.Listar()
    @staticmethod
    def Categoria_ListaId(id):
        return Categorias.Listar_id(id)
    @staticmethod
    def Categoria_ListarId(id):
        return Categorias.Listar_id(id)
    @staticmethod
    def Categoria_Atualizar(id, nome, descricao):
        Atualizando = Produto(id, nome, descricao)
        Categorias.Atualizar(Atualizando)
    @staticmethod
    def Categoria_Excluir(id):
        Excluindo = Categoria(id, "", "")
        Categoria.Excluir(Excluindo)