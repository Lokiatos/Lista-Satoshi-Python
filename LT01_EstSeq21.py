# Objetivo: Receber 4 notas bimestrais de um aluno. Calcular e mostrar a média aritmética. Mostrar a mensagem de acordo com a Média.
# Se a média for>= 6,0 exibir "APROVADO"
# Se a média for >= 3,0 ou <6,0 exibir "EXAME"
# Se a média for <3,0 exibir "RETIDO"
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

nota1 = float(input("Digite aqui o valor da nota do primeiro bimestre: "))
nota2 = float(input("Digite aqui o valor da nota do segundo bimestre: "))
nota3 = float(input("Digite aqui o valor da nota do terceiro bimestre: "))
nota4 = float(input("Digite aqui o valor da nota do quarto bimestre: "))
media = ((nota1 + nota2 + nota3 + nota4) / 4)

if media >= 6:
    print("O aluno teve media de: ", media, " Ele está APROVADO")
elif media >= 3 or media < 6:
    print("O aluno teve media de: ", media, " Ele está de EXAME")
else:
    print("O aluno teve media de: ", media, " Ele está RETIDO")
