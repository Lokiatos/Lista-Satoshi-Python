# Objetivo: Receber um número. Calcular e mostrar os resultados da tabuada desse número.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.19

# Função
def Ftabuada(num, multi):
    result = (multi * num)
    return (result)


# Principal
n = 0
mult = 10
result = 0

n = int(input("Digite o número para sabermos sua tabuada: "))

while mult >= 0:
    print(f'{n} X = {Ftabuada(n, mult)}')  # Laço com print da função
    mult += -1
