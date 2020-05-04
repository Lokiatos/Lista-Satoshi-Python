# Objetivo: Receber os valores de x e y. Efetuar a troca de seus valores e mostrar seus conteúdos.
# Programador: Hugo Leça Ribeiro
# Data da Elaboração: 03/09/2019

x = float(input("Digite aqui o valor de x"))
y = float(input("Digite aqui o valor de y"))
armazenador = x
x = y
y = armazenador

print("O valor atual de x é de: ", x)
print("O valor atual de y é de: ", y)
