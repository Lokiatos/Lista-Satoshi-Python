# Objetivo: Receber 100 números inteiros reais. Verificar e mostrar o maior e o menor Valor. Obs.: Somente valores positivos.
# Programador: Hugo Leça Ribeiro.
# Data de Elaboração: 15.09.2019

maior = 0
menor = 0
n = 0
c = 0

while c <= 99:
    n = (int(input("Digite aqui um número ")))
    if c == 0:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        else:
            if n < menor:
                menor = n
    c = (c + 1)
if menor == maior:
    print("Todos os números são iguais")
else:
    print("O menor número será: ", menor)
    print("O maior número será: ", maior)
