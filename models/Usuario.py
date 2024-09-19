import json
from models.modelo import Modelo
class Usuario:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha
    def set_id(self, id):
        if id < 0: raise ValueError()
    def set_nome(self, nome):
        if nome == "": raise ValueError()
    def set_email(self, email):
        if email == "": raise ValueError()
    def set_fone(self, fone):
        if fone == "": raise ValueError()
    def set_senha(self, senha):
        if senha == "": raise ValueError()
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def get_senha(self):
        return self.__senha
    def ToString(self):
        return f'ID - {self.__id} Nome - {self.__nome} E-mail - {self.__email} Fone - {self.__fone} Senha - {self.__senha}'
    
class Usuarios(Modelo):
    
    @classmethod
    def Abrir(cls, obj):
        cls.objetos = []
        with open("usuarios.json", mode='r') as arquivo:
            usuarios_json = json.load(arquivo)
            for obj in usuarios_json:
                u = Usuario(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
            cls.objetos.append(u)

    @classmethod
    def Salvar(cls):
        with open("usuario.json", mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)

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
