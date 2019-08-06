#Calcular raiz quadrada, dobro e triplo de um numero
num = int(input("Digite um número: "))
d = num * 2
print("O dobro de {} é {}.".format(num,d))
t = num * 3
print("O triplo de {} é {}.".format(num, t))
raiz = num ** (1/2)
print("A raiz quadrada de {} é {:.2f}.".format(num, raiz))
