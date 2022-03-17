# Tarefa - Herança - 2º Certificação - DS202 - PEDRO RODRIGUES MORALLES

from datetime import datetime

class Animal:
    def __init__(self, especie, data_nasc):
        self.especie = especie
        self.data_nasc = data_nasc
    
    def imprimir(self):
        print("Espécie: ", self.especie)
        print("Data de nascimento: ", self.data_nasc)

class AnimalDomestico(Animal):
    def __init__(self, nome):
        self.nome = nome
    
    def imprimir(self):
        print("\nAnimal doméstico\n")
        print("Nome: \t\t\t", self.nome)
        print("Espécie: \t\t", self.especie)
        print("Data de nascimento: \t", self.data_nasc)
        print("-------------------\t --------------------------")

class AnimalSelvagem(Animal):
    def __init__(self, rastreio):
        self.rastreio = rastreio
    
    def imprimir(self):
        print("\nAnimal selvagem\n")
        print("Código de rastreio: \t", self.rastreio)
        print("Espécie: \t\t", self.especie)
        print("Data de nascimento: \t", self.data_nasc)
        print("-------------------\t --------------------------")

class Humano(Animal):
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF
    
    def imprimir(self):
        print("\nHumano\n")
        print("Nome: \t\t\t", self.nome)
        print("Data de nascimento: \t", self.data_nasc)
        print("CPF: \t\t\t", self.CPF)
        print("-------------------\t --------------------------")

AD1 = AnimalDomestico("Tobi")
AD1.especie = "Canis lupus familiaris"
AD1.data_nasc = datetime.now()
AD1.imprimir()

AS1 = AnimalSelvagem("0001")
AS1.especie = "Iguana iguana"
AS1.data_nasc = datetime.now()
AS1.imprimir()

H1 = Humano("Afonso", "000012")
H1.data_nasc = datetime.now()
H1.imprimir()
