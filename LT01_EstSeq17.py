# Objetivo: Calcular a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

rendimento = 12
tempoDePercurso = float(input("Digite aqui o tempo que levou o percurso (em horas): "))
vM = float(input("Digite aqui a velocidade média do automóvel (em km/h): "))
litrosGastos = ((tempoDePercurso * vM) / 12)

print("O total de litros gastos foi de: ", litrosGastos)
