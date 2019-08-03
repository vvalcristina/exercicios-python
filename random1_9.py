#Gere um número aleatório entre 1 e 9 (incluindo 1 e 9).
# Peça ao usuário para adivinhar o número, depois diga se ele adivinhou muito baixo, muito alto ou exatamente certo.

import random
#gerando um numero aleatorio entre 1 e 9
num = random.randint(1,9)

guess=0
count=0



#Enquanto o número digitado é diferente do numero gerado e de exit
while guess != num and guess != "exit":#O usuario digita o numero
#O usuario digita o numero ou pra sair
  guess = input("Você seria capaz de adivinhar um número entre 1 e 9?/n Para sair do jogo, digite 'exit': ")

  if guess == "exit":
      print("================Game Over================")
      break

  guess = int(guess)
  count += 1
#guess(numero digitado)é maior ou menor que o guess(num aleatorio gerado)
  if guess < num:
      print("Este número está muito abaixo!")

  elif guess > num:
      print("Este número está muito acima!")

#Usuário acertou exibe:
  else:
      if count == 1:
          print("Parabéns!!! Você acertou na primeira tentativa!")
      elif count <=3 :
          print("Parabéns! Você acertou em {} tentativas.".format(count))
      elif count > 3 :
        print("Parabéns! Você acertou em {} tentativas.".format(count))
