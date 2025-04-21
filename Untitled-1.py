class Carro:
    def __init__(self,marca, modelo, ano, preco):
        self.marca
        self.modelo
        self.ano
        self.preco
        
    def info_carro(self):
        print(f"{self.marca}{self.modelo}{self.ano}-R${self.preco}")

class CarroUsado(Carro):
    def __init__(self, marca, modelo, ano, preco, km):
        super().__init__(marca, modelo, ano, preco)
        self.km = km
    
    def info_carro(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco} - {self.km} km")

estoque = []

def add_carro():
    tipo = input("tipo de carro (1 - SemiNovo) (2 - Usado)")
    marca = input ("Marca: ")
    modelo = input("Modelo: ")
    ano = input ("Ano: ")
    preco = float(input("Preço: R$ "))

    if tipo == "1":
        carro = Carro(marca, modelo, ano ,preco)
    elif tipo == "2":
        km = int(input("Km rodados: "))
        carro = CarroUsado(marca, modelo, ano, preco, km)
    else:
        print("Tipo inválido")
        return

estoque.append(Carro)
print("Carro adicionado com sucesso!\n")

def lista_carro():
    if not estoque:
        print("Nenhuma carro no estoque.")
    else:
        for i, carro in enumerate(estoque):
            print(f"{i+1}.", end="")
            carro.exibir_info()


