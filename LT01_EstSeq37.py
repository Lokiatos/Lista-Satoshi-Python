# Objetivo: Receba um número inteiro. Calcule e mostre a sére de Fibonacci até o seu N'nésimo termo.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 15.09.2019

c = 0
n = 0
nAnt2 = 0
nAnt = 1
nAt = 0

n = int(input("Digite aqui o número do termo desejado "))

if n <= 0:
    print("Termo inválido")
else:
    if n == 1:
        print("O valor do termo de número 1 é de: ", nAnt2)
    else:
        print("O valor do termo de número 1 é de: ", nAnt2)
        print("O valor do termo de número 2 é de: ", nAnt)
        if n > 2:
            c = 3
            while c <= n:
                nAt = (nAnt2 + nAnt)
                print("O valor do termo de número ", c, "é de: ", nAt)
                nAnt2 = nAnt
                nAnt = nAt
                c = (c + 1)
