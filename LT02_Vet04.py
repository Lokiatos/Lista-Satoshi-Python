# Programador: Hugo Leça Ribeiro
# Data de eblaboração: 23/10/2019

# Criar e coletar em um vetor [30] real, calcular e exibir:
# A média do grupo
# A quantidade de notas acima do grupo
# As posições dos valores abaixo da média do grupo

vet = []
media = 0
notasacima = 0
posicoes = []

for i in range(0, 30, 1):
    vet.append(float(input("Digite aqui um número ")))
    media = media + vet[i]
media = media / 30
for i in range(0, 30, 1):
    if vet[i] > media:
        notasacima += 1
    else:
        posicoes.append(i)
print("A média do grupo é de: ", media)
print("A quantidade de notas acima do grupo é de: ", notasacima)
print("As posições dos valores abaixo da média do grupo são: ", posicoes)
