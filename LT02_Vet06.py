# 'Objetivo: Criar e coletar em um vetor [20] com números aleatórios. Classificar este vetor em ordem crescente e mostrar os dados
# 'A lógica utilizada foi a seguinte:
# 'Vamos supor que o vetor tenha 5 números, do índice 1 até o índice 5, tais como: 5 3 7 2 1'
# 'Eu preciso comparar se o valor do índice 1, ou seja, se o 5 é maior do que o valor do índice 2, ou seja, o número 3'
# 'Neste caso o 5 é maior do que 3, então preciso inverter de posição esses números. Assim, o vetor ficaria: 3 5 7 2 1'
# 'Agora, preciso fazer o mesmo procedimento iniciando do índice 1 ainda - que agora equivale ao número 3'
# '3 é maior do que 5? Não. Então preciso aumentar em 1 o número do índice que eu verificarei, ficando assim: 3 (índice 1) é maior do que o número 7 (índice 3)? Não.
# 'Aumentarei em mais um o índice de verificação. Ficando assim: 3 (índice 1) é maior do que o número 2 (índice 4)? SIM!'
# 'Como 3 é maior do que o 2, então os trocarei de lugar. Ficando assim osso vetor: 2 5 7 3 1'
# 'Farei a mesma coisa com o 2 agora, o comparando com todos os números e trocando de posição caso seja maior do que algum. Nesse caso ele será maior do que o 1 (índice 5), então os trocarei de posição'
# 'Ficando assim: 1 5 7 3 2'
# 'O 1 (índice 1) será comparado com cada outro número, porém, ele não será maior do que nenhum número. Assim, é a hora de esquecermos o índice 1 e passarmos a analisar o índice 2 (que contém o número 5)'
# 'A ordem do nosso vetor vai se alterando passo a passo, deste modo:
# '5 3 7 2 1
# '3 5 7 2 1
# '2 5 7 3 1
# '1 5 7 3 2
# '1 3 7 5 2
# '1 2 7 5 3
# '1 2 5 7 3
# '1 2 3 5 7

# 'Quando chegarmos até o penúltimo termo, devemos parar o laço, concatenar os valores em string e mostrar'

# 'Programador: Hugo Leça Ribeiro
# Data de Elaboração: 13.11.19

vet = []

for i in range(0, 20, 1):
    vet.append(int(input("Digite aqui um número: ")))

for i in range(0, 19, 1):
    for j in range(i + 1, 20, 1):
        if vet[i] > vet[j]:
            vet[i], vet[j] = vet[j], vet[i]
print(vet)
