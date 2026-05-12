print("========== CONTROLE DE TEMPERATURA DAS SALAS ==========")
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala = 1
m_risco = 0
r_criticos = 0

for i in temperaturas:
    soma = sum(i)
    r_criticos = 0

    for j in i:
        if j >= 33:
            r_criticos += 1
            m_risco = r_criticos

    print()

    media = soma / 4

    print(f"Sala: {sala}")
    print(f"Média: {media}")
    print(f"Registros Críticos: {r_criticos}")

    sala += 1

print()
print(f"Sala com maior risco: Sala {m_risco}")
