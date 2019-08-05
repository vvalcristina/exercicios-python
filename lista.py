#Escrever um programa que pegue uma lista de númerose faça uma nova lista apenas do primeiro e último elemento da lista dada.

a = [5, 10, 15, 20, 25]

def lista(x):
    return [x[0], x[-1]]

print(lista(a))
