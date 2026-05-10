# SISTEMA DE CONTROLE DE GASTOS

import csv
import os

arquivo = "gastos.csv"

if not os.path.exists("gastos.csv"):
    open("gastos.csv", "w").close()

#função adicionar gasto
def adicionar_gastos():
    categoria = input("Informe o categoria do gasto: ")
    while True:
        try:
            valor = float(input("Informe o valor do gasto: "))
            break
        except ValueError:
            print("Digite um número válido.")

    print()

    #abrir arquivo em um modo adicionar
    with open(arquivo, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([categoria, valor])

    print("Gasto adicionado!")
    print()

#função ver gastos
def ver_gastos():
    with open(arquivo, "r") as f:
        reader = csv.reader(f)

        linhas = list(reader)

        if not linhas:
            print("\nNenhum gasto registrado. \n")
            return

        print()
        for linha in linhas:
            print(f"Categoria: {linha[0]} | Valor: {float(linha[1]):.2f}")

    print()

#função analisar gastos
def analisar_gastos():
    valores = []

    with open(arquivo, "r") as f:
        reader = csv.reader(f)
        for linha in reader:
            valores.append(float(linha[1]))

    if valores:
        print()
        print(f"Total gasto: {sum(valores)}")
        print(f"Maior valor gasto: {max(valores)}")
        print(f"Média de gasto: {sum(valores)/len(valores)}")
        print()

    else:
        print("Nenhum gasto registrado. ")
        print()

#função limpar limpar registros
def limpar_registros():

    confirmacao = input(f"Tem certeza de que deseja apagar todos os registros? [S]im ou [N]ão. ")

    if confirmacao.lower() == "s":
        open(arquivo, "w").close()
        print("\nRegistros apagados.\n")
    else:
        print("\nOperação cancelada.\n")

#função menu
def menu():
    print(f"----------Sistema de controle de gastos----------")
    print("[1] Adicionar gasto")
    print("[2] Verificar gasto")
    print("[3] Analisar gasto")
    print("[4] Apagar registros")
    print("[5] Sair")

    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas números.\n")
        return 0

#loop principal
while True:
    opcao = menu()

    if opcao == 1:
        adicionar_gastos()
    elif opcao == 2:
        ver_gastos()
    elif opcao == 3:
        analisar_gastos()
    elif opcao == 4:
        limpar_registros()
    elif opcao == 5:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.\n")
