import json
from models.modelo import Modelo

class Produto:
    def __init__(self, id: int, nome: str, valor: float, idCategoria: str):
        self.__id = id
        self.__nome = nome
        self.__valor = valor
        self.__idCategoria = idCategoria

    def __str__(self):
        return f'ID: {self.__id} | Nome: {self.__nome} | Valor: {self.__valor} | Categoria: {self.__idCategoria}'
    
    def set_id(self, id):
        if id < 0: raise ValueError()
        else: self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
    def set_categoria(self, idCategoria):
        if idCategoria == "": raise ValueError()
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_valor(self):
        return self.__valor
    def get_categoria(self):
        return self.__idCategoria

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__valor == x.__valor and self.__idCategoria == x.__idCategoria:
            return True
        return False
    
class Produtos(Modelo):

    @classmethod
    def Salvar(cls):    
        with open("../produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
          with open("../produtos.json", mode="r") as arquivo:
              arquivo_produtos = json.load(arquivo)
              for obj in arquivo_produtos:
                  p = Produto(obj["id"], obj["_Produto__nome"], obj["_Produto__valor"], obj["_Produto__idCategoria"])
                  cls.objetos.append(p)
        except FileNotFoundError:
          pass             
