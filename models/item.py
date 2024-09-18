import json
from models.modelo import Modelo

class Item:
    def __init__(self, id: int, qtd: int, valor: float, id_encomenda: int, id_produto: int):
        self.__id = id
        self.__qtd = qtd
        self.__valor = valor
        self.__idEncomenda = id_encomenda
        self.__idProduto = id_produto
    def __str__(self):
        return f'Id - {self.__id} Quantidade - {self.__qtd} Valor - {self.__valor} Id Encomenda - {self.__idEncomenda} Id produto {self.__idProduto}'

class Itens(Modelo):

    @staticmethod
    def Abrir(cls, obj):
        cls.objetos = []
        with open("item.json", mode= 'r') as arquivo:
            item_json = json.load(arquivo)
            for obj in item_json:
                i = Item(obj["id"], obj["qtd"], obj["valor"], obj["id_encomenda"], obj["id_produto"])
            cls.objetos.append(i)
    
    @staticmethod
    def Salvar(cls):
        return super().Salvar(cls)
    
    @staticmethod
    def Inserir(cls, obj):
        return super().Inserir(cls, obj)
    
    @staticmethod
    def Listar(cls):
        return super().Listar(cls)
    
    @staticmethod
    def Listar_id(cls, obj):
        return super().Listar_id(cls, obj)
    
    @staticmethod
    def Excluir(cls, obj):
        return super().Excluir(cls, obj)
    
    @staticmethod
    def Atualizar(cls, obj):
        return super().Atualizar(cls, obj)
    