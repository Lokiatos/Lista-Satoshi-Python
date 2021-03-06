# Objetivo: Receber a hora de início e de final de um jogo (HH, MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar no outro.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 05.09.2019

horaInicial = int(input("Digite a hora de início do jogo "))
minInicial = int(input("Digite em quantos minutos o jogo se iniciou "))
horaFinal = int(input("Digite a hora em que terminou o jogo "))
minFinal = int(input("Digite aqui com quantos minutos o jogo terminou "))

if (minFinal >= minInicial):  # caso os minutos finais sejam maiores ou iguais aos iniciais
    duracaoMin = (minFinal - minInicial)  # basta subtrair o maior/igual pelo menor/igual
else:
    duracaoMin = ((minFinal + 60) - (minInicial))
    # Caso não sejam maiores, devemos adicionar 60 e subtrair aos minutos iniciais

if (horaFinal > horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:15 até 15:20
    duracaoH = (horaFinal - horaInicial)
elif (horaFinal > horaInicial) and (minInicial > minFinal):  # Exemplo: 10:20 até 15:10
    duracaoH = (horaFinal - horaInicial - 1)

if (horaFinal < horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:10 até 09:20
    duracaoH = ((horaFinal + 24) - (horaInicial))
elif (horaFinal < horaInicial) and (minFinal < minInicial):  # Exemplo: 10:20 até 09:10
    duracaoH = ((horaFinal + 23) - (horaInicial))

if (horaFinal == horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:20 até 10:30
    duracaoH = 0
elif (horaFinal == horaInicial) and (minFinal < minInicial):  # Exemplo: 10:20 até 10:10
    duracaoH = 23

print("O jogo durou: ", duracaoH, "h", duracaoMin, "min")
