#Indicar se a palavra é palindrono
#Palindrono: palavra que tem o mesmo significado de tras pra frente

def palindrono(srt):
    #Reverter a função str
    rev = ''.join(reversed(str))
    #verificar se a palavra é igual
    if (str == rev):
        return True
    return False

str =str(input('Digite uma palavra : \n'))
ans = palindrono(str)

if (ans):
    print("Esta palavra é palindrona")
else:
    print("Esta palavra não é palindrona")
