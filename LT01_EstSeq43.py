# Objetivo: Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10m e cresce 3cm ao ao e Maria tem 1,5m e cresce 2cm ao ano.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 16.09.2019

ana = 110
maria = 150
c = 0

while ana <= maria:
    ana = (ana + 3)
    maria = (maria + 2)
    c = (c + 1)
print("Após ", c, "anos, Ana terá: ", ana, "cm  e Maria terá: ", maria, "cm")
