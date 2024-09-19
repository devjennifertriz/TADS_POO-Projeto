import json
from models.modelo import Modelo

class Usuario:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha

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

    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        else: self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError()
        else: self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError()
        else: self.__fone = fone
    def set_senha(self, senha):
        if senha == "": raise ValueError()
        self.__senha = senha

    def __str__(self):
        return f'ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Fone: {self.__fone} | Senha: {self.__senha}'

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__fone == x.__fone and self.__senha == x.__senha:
            return True
        return False

class Usuarios(Modelo):

    @classmethod
    def Salvar(cls):    
        with open("../usuarios.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
          with open("../usuarios.json", mode="r") as arquivo:
              arquivo_user = json.load(arquivo)
              for obj in arquivo_user:
                  user = Usuario(obj["_Usuario__id"],
                                obj["_Usuario__nome"],
                                obj["_Usuario__email"],
                                obj["_Usuario__fone"],
                                obj["_Usuario__senha"])
                  cls.objetos.append(user)
        except FileNotFoundError:
          pass             