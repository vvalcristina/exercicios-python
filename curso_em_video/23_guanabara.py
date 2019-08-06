#Separando os digitos de um numero
num =int(input("Digite um número: "))
u = num //1 %10
print("Unidade: {}".format(u))
d = num //10 %10
print("Dezena: {}".format(d))
c = num //100 %10
print("Centena: {}".format(c))
m = num //1000 %10
print("Milhar: {}".format(m))
