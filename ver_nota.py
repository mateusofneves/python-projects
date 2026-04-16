# Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas.
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito.
# Cada questão vale um ponto e existem as alternativas A, B, C ou D.
# Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

while True:
    print('======= NOTA DA PROVA =========')
    print('Responda com: A, B, C ou D')

    # Gabarito
    respostas = ['D','A','C','B','A','D','C','C','A','B']

    alternativas = []

    for i in range(10):
        while True:
            resposta = input(f'Questão {i+1}: ').upper()
            if resposta in ['A','B','C','D']:
                alternativas.append(resposta)
                break

            else:
                print('Resposta inválida, digite apenas A, B, C, ou D.')

    acertos = 0
    for i in range(10):
        if alternativas[i] == respostas[i]:
            acertos += 1

    print(f'Acertos: {acertos}/10\n')

    continuar = input('Deseja continuar? [S/N] \n').upper()
    if continuar in 'N':
        break
    else:
        continue
