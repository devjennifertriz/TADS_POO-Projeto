import json
from models.modelo import Modelo
class Usuario:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def Usuario(self, id, nome, email, fone, senha):
        return Usuario
    def ToString(self):
        return f'ID - {self.id} Nome - {self.nome} E-mail - {self.email} Fone - {self.fone} Senha - {self.senha}'
    
class Usuarios(Modelo):
    
    objetos = []
    
    @classmethod
    def Abrir(cls, obj):
        cls.obj_usuarios = []
        with open("usuarios.json", mode='r') as arquivo:
            usuarios_json = json.load(arquivo)
            for obj in usuarios_json:
                u = Usuario(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
            cls.obj_usuarios.append(u)

    @classmethod
    def Salvar(cls):
        with open("usuario.json", mode='w') as arquivo:
            json.dump(cls.obj_usuarios, arquivo, default=vars)

    @classmethod
    def Inserir(cls, obj):
       super().Inserir()

    @classmethod
    def Listar(cls):
        super().Listar()
    
    @classmethod
    def Listar_id(cls, id):
       super().Listar_id()

    @classmethod
    def Excluir(cls, obj):
        super().Excluir()

    @classmethod
    def Atualizar(cls, obj):
       super().Atualizar()

