# Objetivo: Receber a hora de início e de final de um jogo (HH, MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar no outro.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.2019


# Procedimento
def p_duracao(horaInicial, minInicial, horaFinal, minFinal):
    duracao_hora = 0
    if (minFinal >= minInicial):  # caso os minutos finais sejam maiores ou iguais aos iniciais
        duracao_min = (minFinal - minInicial)  # basta subtrair o maior/igual pelo menor/igual
    else:
        duracao_min = ((minFinal + 60) - (minInicial))
        # Caso não sejam maiores, devemos adicionar 60 e subtrair aos minutos iniciais

    if (horaFinal > horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:15 até 15:20
        duracao_hora = (horaFinal - horaInicial)
    elif (horaFinal > horaInicial) and (minInicial > minFinal):  # Exemplo: 10:20 até 15:10
        duracao_hora = (horaFinal - horaInicial - 1)

    if (horaFinal < horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:10 até 09:20
        duracao_hora = ((horaFinal + 24) - (horaInicial))
    elif (horaFinal < horaInicial) and (minFinal < minInicial):  # Exemplo: 10:20 até 09:10
        duracao_hora = ((horaFinal + 23) - (horaInicial))

    if (horaFinal == horaInicial) and (minFinal >= minInicial):  # Exemplo: 10:20 até 10:30
        duracao_hora = 0
    elif (horaFinal == horaInicial) and (minFinal < minInicial):  # Exemplo: 10:20 até 10:10
        duracao_hora = 23

    print("O jogo durou: ", duracao_hora, "h", duracao_min, "min")


# Principal
horaInicial = int(input("Digite a hora de início do jogo: "))
minInicial = int(input("Digite em quantos minutos o jogo se iniciou: "))
horaFinal = int(input("Digite a hora em que terminou o jogo: "))
minFinal = int(input("Digite aqui com quantos minutos o jogo terminou: "))
p_duracao(horaInicial, minInicial, horaFinal, minFinal)  # Chamamento do Procedimento
