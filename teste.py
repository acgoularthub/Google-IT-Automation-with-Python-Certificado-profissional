class Vehicle:
    wheels = 4
    door = 5
    color = ""
    airbag = ""

carro = Vehicle()
carro.color = input("Digite a cor do carro: ")
carro.airbag = input("Digite o tipo de airbag: ")
print("_____________________________________________________")
print(carro.color)
print(carro.airbag)