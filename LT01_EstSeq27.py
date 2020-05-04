# Receber o número de voltas, a extensão do circuito (em metros) e o tempo de duração (em minutos). Calcular e mostrar a velocidade média em km/h.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 05.09.2019

voltas = float(input("Digite aqui o número de voltas do circuito: "))
extensao = float(input("Digite aqui a extensão (em metros) do circuito: "))
duracao = float(input("Digite aqui a duração (em minutos) que levou para completar o percurso: "))

vm = ((voltas * extensao) / 1000) / (duracao / 60)

print("A velocidade média é de: ", vm, "km/h")
