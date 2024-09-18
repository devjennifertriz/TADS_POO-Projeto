import json
from models.modelo import Modelo

class Pedido:
    def __init__(self, id: int, endereçoEntrega: str, status: str, valorTotal: int, qtdProduto: int, idProduto: int, idUsuario: int):
        self.__id = id
        self.__endereco = endereçoEntrega
        self.__status = status
        self.__valorTotal = valorTotal
        self.__qtdProduto = qtdProduto
        self.__idProduto = idProduto
        self.__idUsuario = idUsuario
    def __str__(self):
        return f'ID - {self.__id} Endereço - {self.__endereco} Status - {self.__status} Valor Total - {self.__valorTotal} Quantidade - {self.__qtdProduto} IdProduto{self.__idProduto} IdUsuario - {self.__idUsuario}'
    
class Pedidos(Modelo):

    @staticmethod
    def Abrir(cls, obj):
        cls.objetos = []
        with open("pedido.json", mode='r') as arquivo:
            pedido_json = json.load(arquivo)
            for obj in pedido_json:
                en = Pedido(obj['"Id'], obj['"endereçoEntrega'], obj['"status'], obj['"valorTotal'], obj['"qtdProduto'], obj['"idProduto'], obj['"idUsuario'])
        cls.objetos.append(en)

    @staticmethod
    def Salvar(cls):
        with open("pedido.json", mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
        
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
