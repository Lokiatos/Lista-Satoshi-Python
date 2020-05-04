# Objetivo: Receba um número inteiro. Calcule e mostre a sére de Fibonacci até o seu N'nésimo termo.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 25.10.2019


# Função
def Ffibo(nAnt, nAnt2):
    global nAt
    nAt = 0
    while c <= n:
        nAt = (nAnt2 + nAnt)
        return (nAt)


# Principal
c = 0
nAnt2 = 0
nAnt = 1
n = int(input('Digite aqui o número do termo desejado: '))
if n <= 0:
    print('Termo inválido')
else:
    if n == 1:
        print(f'O valor do termo de número 1 é de: {nAnt2}')  # Caso o número seja 1, então o termo será 0
    else:
        print(f'O valor do termo de número 1 é de: {nAnt2}')  # Número 2 = termo 0 e termo 1
        print(f'O valor do termo de número 2 é de: {nAnt}')
        if n > 2:
            c = 3
            while c <= n:
                print(f'O valor do termo de número {c} é de: {Ffibo(nAnt, nAnt2)}')
                nAnt2 = nAnt
                nAnt = nAt
                c += 1
