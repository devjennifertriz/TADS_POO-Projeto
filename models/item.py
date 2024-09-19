import json
from models.modelo import Modelo

class Item:
    def __init__(self, id: int, qtd: int, valor: float, id_encomenda: int, id_produto: int):
        self.__id = id
        self.__qtd = qtd
        self.__valor = valor
        self.__idEncomenda = id_encomenda
        self.__idProduto = id_produto
    def set_id(self, id):
        if id < 0: raise ValueError()
    def set_qtd(self, qtd):
        if qtd < 0: raise ValueError()
    def set_valor(self, valor):
        if valor < 0: raise ValueError()
    def set_idEncomenda(self, idEncomenda):
        if idEncomenda < 0: raise ValueError()
    def set_idProduto(self, idProduto):
        if idProduto < 0: raise ValueError()
    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_valor(self):
        return self.__valor
    def get_idEncomenda(self):
        return self.__idEncomenda
    def get_idProduto(self):
        return self.__idProduto
    def __str__(self):
        return f'ID: {self.__id} | Quantidade: {self.__qtd} | Valor: {self.__valor} | IdEncomenda: {self.__idEncomenda} | IdProduto {self.__idProduto}'
    

class Itens(Modelo):

    @classmethod
    def Salvar(cls):    
        with open("../itens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
          with open("../itens.json", mode="r") as arquivo:
              arquivo_itens = json.load(arquivo)
              for obj in arquivo_itens:
                  i = Itens(obj["id"], obj["qtd"], obj["valor"], obj["id_encomenda"], obj["id_produto"])
                  cls.objetos.append(i)
        except FileNotFoundError:
          pass    