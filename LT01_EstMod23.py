# Objetivo: Receber 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.05.2019


# Procedimento
def p_ordenar(number1, number2, number3, number4):
    if (number1 < number2 < number3) and (number4 != number1) and (number4 != number2) and (number4 != number3):
        if number4 < number1:
            print(f'Os números em ordem crescente são1: {number4}, {number1}, {number2} e {number3}')
        else:
            if (number1 < number4) and (number4 < number2):
                print(f'Os números em ordem crescente são: {number1}, {number4}, {number2} e {number3}')
            else:
                if (number2 < number4) and (number4 < number3):
                    print(f'Os números em ordem crescente são: {number1}, {number2}, {number4} e {number3}')
                else:
                    print(f'Os números em ordem crescente são: {number1}, {number2}, {number3} e {number4}')
    elif (number4 == number1) or (number4 == number2) or (number4 == number3):
        print('O quarto número é igual a algum outro número, digite novamente')
    else:
        print('Você não digitou os três primeiros números em ordem crescente')


# Principal
print('A seguir você terá que digitar 3 números em ordem crescente, e um quarto número qualquer')
n1 = (float(input('Digite aqui o primeiro número: ')))
n2 = (float(input('Digite aqui o segundo número: ')))
n3 = (float(input('Digite aqui o terceiro número: ')))
n4 = (float(input('Digite aqui o quarto número: ')))

p_ordenar(n1, n2, n3, n4)  # Chamamento do Procedimento
