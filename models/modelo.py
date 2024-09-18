import json
from abc import ABC, abstractmethod

class Modelo(ABC):
    objetos = []

    @staticmethod
    def Abrir(cls, obj):
        pass

    @staticmethod
    def Salvar(cls):
        pass

    @staticmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
            id += 1
        obj.id = id 
        cls.objetos.append(obj)
        cls.Salvar()

    @staticmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos
    
    @staticmethod
    def Listar_id(cls, obj):
        cls.Abrir()

    