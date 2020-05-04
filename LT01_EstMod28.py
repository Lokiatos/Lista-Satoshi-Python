# Objetivo: Receber o preço atual e a média mensal de um produto. Calcular e mostrar o novo preço, sabendo que:
# Se Venda Mensal < 500 e Preço Atual < 30, então o Preço Novo será de + 10%.
# Se Venda Mensal for >= 500 e  < 1000, e o Preço Atual for >=30 e < 80, então o Preço Novo será de +15%.
# Se Vensa Mensal for >= 1000 e o Preço Atual for >= 80, então o Preço Novo será de - 5%.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 27.10.2019


# Procedimento
def p_preconovo(vendaMensal, precoAtual):
    precoNovo = 0
    if (vendaMensal < 500) and (precoAtual < 30):
        precoNovo = (precoAtual * 1.1)
    elif (vendaMensal >= 500 and vendaMensal < 1000) and (precoAtual >= 30 and precoAtual < 80):
        precoNovo = (precoAtual * 1.15)
    elif (vendaMensal >= 1000) and (precoAtual >= 80):
        precoNovo = (precoAtual * 0.95)
    else:
        precoNovo = (precoAtual)

    print("O novo preço do produto será de: ", precoNovo)


# Principal
vendaMensal = float(input("Digite aqui a quantidade de venda mensal: "))
precoAtual = float(input("Digite aqui o preço atual do produto: "))
p_preconovo(vendaMensal, precoAtual)  # Chamamento do Procedimento
