#Achar seno, cosseno e tangente de um angulo
import math
ang = float(input("Digite um ângulo: "))
sen = print("O seno de {:.0f} é {:.1f}.".format(ang, math.sin(math.radians(ang))))
cos = print("O cosseno de {:.0f} é {:.1f}.".format(ang, math.cos(math.radians(ang))))
tan = print("A tangente de {:.0f} é {:.1f}.".format(ang, math.tan(math.radians(ang))))
