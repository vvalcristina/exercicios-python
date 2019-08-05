#Programa que lê algo pelo teclado e mostre seu tipo primitivo  e todas as informações sobre elemento
var= input("Digite algo:")
#var é um objeto, após o objeto é o método
#todo objeto string é composto por métodos
print("O tipo primitivo é:",type(var))
print("Só tem espaços? ", var.isspace())
print("É um número? ", var.isnumeric())
print("É alfabético? ", var.isalpha())
print("É alfanumérico? ", var.isalnum())
print("Está em maiúsculas? ", var.isupper())
print("Está em minúsculas? ",var.islower())
print("Está capitalizada? ", var.istitle())
