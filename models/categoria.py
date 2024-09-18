import json
from models.modelo import Modelo

class Categoria:
    def __init__(self,id: int, nome: str, descricao: str):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
    def __str__(self):
        return f'ID - {self.__id} Nome - {self.__nome} Descrição - {self.__descricao}'
    
class Categorias(Modelo):

    @staticmethod
    def Abrir(cls, obj):
        cls.objetos = []
        with open("categoria.json", mode='r') as arquivo:
            categoria_json = json.load(arquivo)
            for obj in categoria_json:
                cat = Categoria(obj['"Id'], obj['"nome'], obj['"descricao'])
        cls.objetos.append(cat)

    @staticmethod
    def Salvar(cls):
        with open("categorias.json", mode='w') as arquivo:
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
    