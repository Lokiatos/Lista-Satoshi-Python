# Objetivo: Receber 2 ângulos de um triângulo. Calcular e mostrar o valor do 3º ângulo.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

ang1 = float(input("Digite aqui o valor do 1º ângulo "))
ang2 = float(input("Digite aqui o valor do 2º ângulo "))
ang3 = (180 - (ang1 + ang2))

print("O valor do terceiro ângulo é de: ", ang3, "º")
