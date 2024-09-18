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



