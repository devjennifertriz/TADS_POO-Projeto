import json
from models.modelo import Modelo

class Produto:
    def __init__(self, id: int, nome: str, valor: float, categoria: str):
        self.__id = id
        self.__nome = nome
        self.__valor = valor
        self.__categoria = categoria
    def __str__(self):
        return f'ID - {self.__id} Nome - {self.__nome} Valor - {self.__valor} Categoria - {self.__categoria}'

class Produtos(Modelo):

    @staticmethod
    def Abrir(cls, obj):
        cls.objetos = []
        with open("produtos.json", mode='r') as arquivo:
            produtos_json = json.load(arquivo)
            for obj in produtos_json:
                pr = Produto(obj['"Id'], obj['"nome'], obj['"valor'], obj['"categoria'])
        cls.objetos.append(pr)

    @staticmethod
    def Salvar(cls):
        with open("produtos.json", mode='w') as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)
        
    @staticmethod
    def Inserir(cls, obj):
        return super().Inserir(cls, obj)

    @staticmethod
    def Listar(cls):
        return super().Listar(cls)

    @staticmethod
    def Listar_id(cls):
        return super().Listar_id(cls, id)

    @staticmethod
    def Excluir(cls, obj):
        return super().Excluir(cls, obj)

    @staticmethod
    def Atualizar(cls, obj):
        return super().Atualizar(cls, obj)
