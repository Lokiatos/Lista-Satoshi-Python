# Objetivo: Receber 3 coeficientes: A, B e C de uma equação do 2º grau da fórmula AX² + BX + C = 0. Verificar e mostrar a existência de raízes reais e se caso exista, calcular e mostrar.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.2019


# Procedimento
def p_bhaskara(A, B, C):
    delta = (B ** 2) - (4 * A * C)
    x1 = (-B + (delta ** 0.5)) / (2 * A)
    x2 = (-B - (delta ** 0.5)) / (2 * A)
    if delta < 0:
        print('Não há raízes reais')
    elif delta > 0:
        print(f'A primeira raiz será de: {x1}')
        print(f'A segunda raiz será de: {x2}')
    else:
        print(f'Só terá uma raiz, que será de: {x1}')


# Principal
A = float(input('Digite aqui o valor de A: '))
B = float(input('Digite aqui o valor de B: '))
C = float(input('Digite aqui o valor de C: '))

p_bhaskara(A, B, C)  # Chamamento do Procedimento
