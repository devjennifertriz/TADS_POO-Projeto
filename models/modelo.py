from abc import ABC, abstractmethod

class Modelo(ABC):
    objetos = []

    @classmethod
    @abstractmethod
    def Abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def Salvar(cls):
        pass

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
            id += 1
        obj.id = id 
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos
    
    @classmethod
    def Listar_id(cls, obj):
        cls.Abrir()
        for x in cls.objetos:
            if x.id == id: return x
        return None 

    @classmethod
    def Excluir(cls, obj):
        x = cls.Listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.Salvar()

    @classmethod
    def Atualizar(cls, obj):
        x = cls.Listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.append(obj)
            cls.Salvar()
