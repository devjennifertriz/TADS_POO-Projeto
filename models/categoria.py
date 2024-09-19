import json
from models.modelo import Modelo

class Categoria:
    def __init__(self, id: int, nome: str, desc: str):
        self.__id = id
        self.__nome = nome
        self.__desc = desc
    def set_id(self, id):
        if id < 0: raise ValueError()
    def set_nome(self, nome):
        if nome == "": raise ValueError()
    def set_descricao(self, desc):
        if desc == "": raise ValueError()
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_desc(self):
        return self.__desc

    def __eq__(self, x):
        if self.__id == x.__id and self.__nome == x.__nome and self.__desc == x.__desc:
            return True
        return False
    
    def __str__(self):
        return f'ID - {self.__id} Nome - {self.__nome} Descrição - {self.__desc}'
    
class Categorias(Modelo):

    @classmethod
    def Salvar(cls):    
        with open("../categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
          with open("../categorias.json", mode="r") as arquivo:
              arquivo_categorias = json.load(arquivo)
              for obj in arquivo_categorias:
                  cat = Categoria(obj["_Categoria__id"], obj["_Categoria__nome"], obj["_Categoria__desc"])
                  cls.objetos.append(cat)
        except FileNotFoundError:
          pass    