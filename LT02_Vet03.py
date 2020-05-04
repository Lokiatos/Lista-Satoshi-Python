# Programador: Hugo Leça Ribeiro
# Data de elaboração: 23/10/2019

# Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. Concatenar #esses valores em um 3º vetor (VT3[6]) e mostrar os seus dados. P. ex:
# VT1 |1|2|3|     VT2 |4|5|6|        VT3 1|2|3|4|5|6

i = 0
vet1 = []
vet2 = []
vet3 = []

for i in range(0, 3, 1):
    vet1.append(int(input("Digite aqui um número para o vetor 1: ")))
    vet2.append(int(input("Digite aqui um número para o vetor 2: ")))
for i in range(0, 3, 1):
    vet3 = vet1 + vet2

print(vet3)
