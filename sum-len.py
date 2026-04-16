# Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel
# [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08].
# Com esses valores, faça um programa que calcule a média de gastos.
# Com os mesmos dados da questão anterior, defina:
# quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

#lista com valores armazenados
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

#calculo media
media = sum(gastos) / len(gastos)

#variavel para ver quais valores são acima de 3000
acima_3000 = 0

for valor in gastos:
    if valor > acima_3000:
        acima_3000 += valor

#calculo da porcentagem
porcentagem = (acima_3000 / len(gastos)) * 100

print(f"Média de gastos: R$ {media:.2f}")
print(f"Compras acima de R$ 3000: {acima_3000}")
print(f"Porcentagem: {porcentagem:.2f}%")
