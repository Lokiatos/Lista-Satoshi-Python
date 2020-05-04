# Objetivo: Receber os valores de 2 catetos de um triângulo retângulo. Calcular e mostrar a hipotenusa.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

cat1 = float(input("Digite aqui o valor de um cateto: "))
cat2 = float(input("Digite aqui o valor do outro cateto: "))
hip = (((cat1 ** 2) + (cat2 ** 2)) ** 0.5)

print("O valor da hipotenusa é de: ", hip)
