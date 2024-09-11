import json

class Usuario:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def Usuario(self, id, nome, email, fone, senha):
        return Usuario
    def ToString(self):
        return f'ID - {self.id} Nome - {self.nome} E-mail - {self.email} Fone - {self.fone} Senha - {self.senha}'
    
class Usuarios:
    objetos = []
    @classmethod
    def Abrir(cls, obj):
        cls.obj_usuarios = []
        with open("usuarios.json", mode='r') as arquivo:
            usuarios_json = json.load(arquivo)
            for obj in usuarios_json:
                u = Usuario(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
            cls.obj_usuarios.append(u)

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for x in cls.obj_usuarios:
            if x.id > id: id = x.id
        id += 1
        obj.id = id
        cls.obj_usuarios.append(obj)
        cls.Salvar()

    @classmethod
    def Salvar(cls):
        with open("usuario.json", mode='w') as arquivo:
            json.dump(cls.obj_usuarios, arquivo, default=vars)

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.obj_usuarios
    
    @classmethod
    def Listar_id(cls, id):
        cls.Abrir()
        for x in cls.obj_usuarios:
            if x.id == id: return x
        return None
    
    @classmethod
    def Excluir(cls, obj):
        x = cls.Listar_id(obj.d)
        if x != None:
           cls.obj_usuarios.remove(x)
           cls.Salvar()


    @classmethod
    def Atualizar(cls, obj):
        x = cls.Listar_id(obj.id)
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
            cls.Salvar()

class Encomenda:
    def __init__(self, id, enderecoEntrega, status, valorTotal,qtdProduto, idProduto, idUsuario):
        self.id = id
        self.enderecoEntrega = enderecoEntrega
        self.status = status
        self.valorTotal = valorTotal
        self.qtdProduto = qtdProduto
        self.idProduto = idProduto
        self.idUsuario = idUsuario
    def __str__(self):
        return f'Id - {self.id} Endereço - {self.enderecoEntrega}  Status - {self.status} Valor Total - {self.valorTotal} Quantidade Produto - {self.qtdProduto} Id Produto - {self.idProduto} Id Usuário - {self.idUsuario}'

class Encomendas:
    @staticmethod
    def Inserir_Encomenda(cls, obj):
        super().Abrir(cls)