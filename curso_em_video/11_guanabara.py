#Calcular a area de uma parede e o quanto de tinta é necessário, sabendo que a
#cada 2m² utiliza-se 1L de tinta
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = alt*larg
tinta = area / 2
print("A parede tem dimensão de {}x{} e sua área é de {:.2f}m², portanto, necessita de {}L para ser pintada".format(larg, alt,area, tinta))
