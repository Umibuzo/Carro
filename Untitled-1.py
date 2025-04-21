class Carro:
    def __init__(self, marca, modelo, ano, preco, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.km = km

    def info_carro(self):
        print(f"{self.marca} {self.modelo} {self.ano} -R$ {self.preco} Km {self.km}")

class CarroUsado(Carro):
    def __init__(self, marca, modelo, ano, preco, km):
        super().__init__(marca, modelo, ano, preco, km)
        self.km = km
    
    def info_carro(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) - R$ {self.preco} - Km{self.km}")

estoque = []

def add_carro():
    tipo = input("tipo de carro (1 - SemiNovo) (2 - Usado) \n Opção: ")
    marca = input ("Marca: ")
    modelo = input("Modelo: ")
    ano = input ("Ano: ")
    preco = float(input("Preço: R$ "))
    km = int(input("Km Rodados: "))

    if tipo == "1":
        carro = Carro(marca, modelo, ano ,preco, km)
        estoque.append(carro)
        print("Carro Seminovo adicionado com sucesso!\n")
    elif tipo == "2":
        carro = CarroUsado(marca, modelo, ano, preco, km)
        estoque.append(carro)
        print("Carro Usado adcicionado com sucesso")
    else:
        print("Tipo inválido")
        return
    

def lista_carro():
    if not estoque:
        print("Nenhum carro no estoque. Adicione um carro usando a opção 1 do menu.\n")
    else:
        print("=== Lista de Carros no Estoque ===")
        for i, carro in enumerate(estoque):
            print(f"{i + 1}. {carro.marca} {carro.modelo} ({carro.ano}) - R$ {carro.preco:.2f} - {carro.km} km")
        print() 

def remove_carro():
    if  estoque:
        escolha = int(input("Número do carro para remover: ")) - 1
        if 0 <= escolha < len(estoque):
            removido = estoque.pop(escolha)
            print(f"{removido.modelo} removido com sucesso!\n")

def menu():
    while True:
        print("=== Sistema de Revenda de Carros ===")
        print("1. Adicionar carro")
        print("2. Listar carros")
        print("3. Remover carro")
        print("4. sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            add_carro()
        elif escolha == "2":
            lista_carro()
        elif escolha == "3":
            remove_carro()
        elif escolha == "4":
            print("saindo . . .")
            break
        else:
            print("opção inválida. \n")
menu()
