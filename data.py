#Programa para dizer em que ano o usuario fara 100 anos

from datetime import datetime
name = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))
anocem = int((100-idade) + datetime.now().year)
print ('Oi %s, você tem %s anos. Você completará 100 anos em %s.' %(name, idade,anocem))

#Indicar o numero de vezes que o usuario deseja que a mensagem seja repetida
repeat =int(input('Digite o numero de copias: '))
exer1=('Oi %s, você tem %s anos. Você completará 100 anos em %s.\n' %(name, idade,anocem))
print(repeat*exer1)
