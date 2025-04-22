import uuid

# =====================CLASSES============================
class Carro: #classe principal 
    def __init__(self, marca, modelo, ano, preco, km):
        self.id = str(uuid.uuid4())
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.km = km

    def info_carro(self):
        print(f"{self.marca} {self.modelo} {self.ano} -R$ {self.preco} Km {self.km}")

class CarroUsado(Carro): # Carro Seminovo
    def __init__(self, marca, modelo, ano, preco, km):
        super().__init__(marca, modelo, ano, preco, km)
        self.km = km
    
    def info_carro(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco} - Km{self.km}")

class Usuario:
    def __init__(self, nome, email,senha):
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.estoque = [] #estoque do usuario

    def add_carro(self, carro):
        self.estoque.append(carro)

    def remove_carro(self, index):
        if 0 <= index < len(self.estoque):
            return self.estoque.pop(index)
        return None

estoque = []


# =======================CADASTRO=======================
usuarios = []

def registrar():
    print("\n=== Registro de Usuário ===")
    nome = input ("Nome: ")
    email = input ("Email: ")
    senha = input ("Senha: ")

    for u in usuarios:
        if u.email == email:
            print("Email já registrado.\n")
            return novo
        
    novo = Usuario(nome, email, senha)
    usuarios.append(novo)
    print("Registro concluído!\n")
    return novo

def login():
    print("\n=====Login====")
    email = input ("Email: ")
    senha = input ("Senha: ")
    for u in usuarios:
        if u.email == email and u.senha == senha:
            print(f"Bem-vindo {u.nome}!\n")
            return u
    print("Login inválido.\n")
    return u

# ====================== ADD CARRO E REMOV ===========================

def add_carro(usuario):
    tipo = input("tipo de carro (1 - SemiNovo) (2 - Usado) \n Opção: ")
    marca = input ("Marca: ")
    modelo = input("Modelo: ")
    ano = input ("Ano: ")
    preco = float(input("Preço: R$ "))
    km = int(input("Km Rodados: "))

    if tipo == "1": #seminovo
        carro = Carro(marca, modelo, ano ,preco, km)

    elif tipo == "2": #usado
        carro = CarroUsado(marca, modelo, ano, preco, km)

    else:
        print("Tipo inválido")
        return
    
    usuario.add_carro(carro)
    print("Carro adicionado com sucesso!\n")


def lista_carro(usuario):
    if not usuario.estoque:
        print("Nenhum carro no estoque.\n")
    else:
        print("=== Lista de Carros no Estoque ===")
        for i, carro in enumerate(usuario.estoque):
            print(f"{i+1}. {carro.marca} {carro.modelo} ({carro.ano}) - R$ {carro.preco:.2f} - {carro.km} km")
        print() 

def remove_carro(usuario):
    if  usuario.estoque:
        lista_carro(usuario)
        escolha = int(input("Número do carro para remover: ")) - 1
        removido = usuario.remove_carro(escolha)

        if removido:
            print (f"{removido.modelo} removido com sucesso!\n")

        else:
            print("índice inválido.\n")

    else:
        print("Você não tem carros para remover.\n")

# ===================== MENUS ============================

def menu_usuario(usuario):
    while True:
        print("=== Sistema de Revenda de Carros ===")
        print("1. Adicionar carro")
        print("2. Listar carros")
        print("3. Remover carro")
        print("4. sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            add_carro(usuario)
        elif escolha == "2":
            lista_carro(usuario)
        elif escolha == "3":
            remove_carro(usuario)
        elif escolha == "4":
            print("Saindo da conta \n")
            break
        else:
            print("Opção inválida. \n")

        
def menu_principal():
    while True:
        print("=== Sistema de Revenda de Carros ===")
        print("1. Login")
        print("2. Registrar")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            user = login()
            if user:
                menu_usuario(user)
        elif escolha =="2":
            user = registrar()
            if user:
                menu_usuario(user)
        elif escolha == "3":
            print("Encerrando sistema...\n")
            break
        else:
            print("Opção inválida\n")

menu_principal()

