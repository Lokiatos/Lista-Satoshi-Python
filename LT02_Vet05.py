# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 23/10/2019

# Criar e voletar em um vetor [20] inteiro. Calcule e exiba, segundo:
# SOMA de 1 até 10 (A[1] - A[21-1])

vet = []
soma = 0
i = 1
c = 19

for i in range(0, 20, 1):
    vet.append(int(input("Digite aqui um número: ")))  # Receberá 20 valores no vet
for i in range(0, 10, 1):
    soma = soma + vet[i] - vet[c]  # Fará 10 vezes a soma dos números
    c -= 1  # Diminuirá em 1 a posição no final, ficando do número 19 até 09
print("A soma dos números será: ", soma)
