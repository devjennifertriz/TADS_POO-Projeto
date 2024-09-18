from models.Usuario import Usuario, Usuarios

class View:
    @staticmethod
    def Usuario_Inserir(nome, email, fone, senha):
        Inserindo = Usuario(0, nome, email, fone, senha)
        Usuarios.Inserir(Inserindo)
    @staticmethod
    def Usuario_Listar():
        return Usuarios.Listar()
    @staticmethod
    def Usuario_Atualizar(id, nome, email, fone, senha):
        Atualizando = Usuario(id, nome, email, fone, senha)
    @staticmethod
    def Usuario_Excluir(id):
        Excluindo = Usuario(id, "semnome", "sememail", "")
        Usuarios.Excluir(Excluindo)
