#Escreva um programa gerador de senhas a partir de uma serie de caracteres

#Importando a biblioteca Random https://docs.python.org/3/library/random.html
import random
usuario_input = int(input("Por favor, digite o tamanho da senha desejada: "))

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.;:?!@#$%¨&*"
#Funçaõ que define a senha
def senha(a):
    #random.choice : retorna um elemento aleatorio de uma sequencia nao vazia
    saida = [] #lista de saída de senha
    i = 1
    while i <= a:
        #b retorna uma senha aleatoria da lista da variável caracteres
        b = random.choice(caracteres)
        #append: adiciona qualquer valor completo(objeto ou lista inteira e não seus elementos)
        saida.append(b)
        #a variavel saida retorna a lista inteira da variavel b
        i += 1
    print("Sua senha é: " + "".join(saida))

senha(usuario_input)
