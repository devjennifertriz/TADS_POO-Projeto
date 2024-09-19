import json
from models.modelo import Modelo

class Encomenda:
    def __init__(self, id: int, endereçoEntrega: str, status: str, valorTotal: int, idUsuario: int):
        self.__id = id
        self.__endereco = endereçoEntrega
        self.__status = status
        self.__valorTotal = valorTotal
        self.__idUsuario = idUsuario
    def __str__(self):
        return f'ID - {self.__id} Endereço - {self.__endereco} Status - {self.__status} Valor Total - {self.__valorTotal} IdUsuario - {self.__idUsuario}'
    def set_id(self, id):
        if id < 0: raise ValueError()
    def set_endereco(self, enderecoEntrega):
        if enderecoEntrega == "": raise ValueError()
    def set_status(self, status):
        if status == "": raise ValueError()
    def set_valor(self, valorTotal):
        if valorTotal < 0: raise ValueError()
    def set_idUsuario(self, idUsuario):
        if idUsuario == "": raise ValueError()
    def get_id(self):
        return self.__id
    def get_enderco(self):
        return self.__endereco
    def get_status(self):
        return self.__status
    def get_valorTotaç(self):
        return self.__valorTotal
    def get_idUsuario(self):
        return self.__idUsuario

class Encomendas(Modelo):

    @classmethod
    def Salvar(cls):    
        with open("../encomenda.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
          with open("../encomenda.json", mode="r") as arquivo:
              arquivo_encomenda = json.load(arquivo)
              for obj in arquivo_encomenda:
                  e = Encomenda(obj["id"], obj["nome"], obj["email"], obj["fone"])
                  cls.objetos.append(e)
        except FileNotFoundError:
          pass    