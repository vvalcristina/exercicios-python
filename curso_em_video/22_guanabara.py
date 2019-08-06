#Aprendendo a manipular strings
nome = str(input("Digite seu nome completo: "))
print("Analisando ...")
print("Seu nome em maiúsculas é {}: ".format(nome.upper()))
print("Seu nome em minúsculas é {}: ".format(nome.lower()))
print("Seu nome tem {} letras".format(len(''.join(nome.split()))))
pal =nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(pal[0], len(pal[0])))
