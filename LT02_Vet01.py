# Criar e Coletar um vetor [50] inteiro. Calcular e exibir:
# A média dos valores entre 10 e 200
# A soma dos números ímpares

vet = []
i = 0
media = 0
somaimp = 0
cmedia = 0

for i in range(0, 10, 1):
    vet.append(int(input("Digite aqui um número ")))
    if vet[i] > 10 and vet[i] < 200:
        media = media + vet[i]
        cmedia = cmedia + 1
    if vet[i] % 2 == 1:
        somaimp = somaimp + vet[i]
media = media / cmedia
print("A média dos números entre 10 e 200 é: ", media)
print("A soma dos números ímpares é de: ", somaimp)
