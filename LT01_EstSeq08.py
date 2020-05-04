# Objetivo: Receber o valor de um depósito em poupança. Calcular e mostrar o valor após 1 mês de aplicação sabendo que rende 1,3% ao mês.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

Mes = 1
Rendimento = (1.3 / 100)

ValorDeDeposito = float(input("Digite aqui o valor depositado "))
ValorFinal = ValorDeDeposito + (ValorDeDeposito * Mes * Rendimento)

print("O valor com os rendimentos é de: ", ValorFinal)
