# MISSION CONTROL AI
# Global Solution - FIAP

nome_missao = "Orion Nexus"
equipe = "Equipe NextBand"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura Interna",
    "Comunicação com a Base",
    "Sistema de Energia",
    "Suporte de Oxigênio",
    "Estabilidade Operacional"
]


# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


# CLASSIFICAÇÃO

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."


def gerar_recomendacao(risco):
    if risco <= 2:
        return "Manter operação normal."
    elif risco <= 5:
        return "Monitorar sistemas em atenção."
    else:
        return "Ativar plano de contingência imediatamente."


# PROCESSAMENTO

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

temperaturas = []
comunicacoes = []
baterias = []
oxigenios = []
estabilidades = []

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    temperaturas.append(temperatura)
    comunicacoes.append(comunicacao)
    baterias.append(bateria)
    oxigenios.append(oxigenio)
    estabilidades.append(estabilidade)

    status_temp, risco_temp = analisar_temperatura(temperatura)
    status_com, risco_com = analisar_comunicacao(comunicacao)
    status_bat, risco_bat = analisar_bateria(bateria)
    status_oxi, risco_oxi = analisar_oxigenio(oxigenio)
    status_est, risco_est = analisar_estabilidade(estabilidade)

    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += risco_temp
    pontuacao_areas[1] += risco_com
    pontuacao_areas[2] += risco_bat
    pontuacao_areas[3] += risco_oxi
    pontuacao_areas[4] += risco_est

    print(f"\nCICLO {i + 1}")
    print("-" * 40)

    print(f"Temperatura: {temperatura}°C | {status_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com}")
    print(f"Bateria: {bateria}% | {status_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est}")

    print(f"\nPontuação de risco: {risco_total}")
    print(f"Classificação: {classificar_ciclo(risco_total)}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")


# RELATÓRIO FINAL

media_temperatura = sum(temperaturas) / len(temperaturas)
media_comunicacao = sum(comunicacoes) / len(comunicacoes)
media_bateria = sum(baterias) / len(baterias)
media_oxigenio = sum(oxigenios) / len(oxigenios)
media_estabilidade = sum(estabilidades) / len(estabilidades)

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

ciclos_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

indice_area = pontuacao_areas.index(max(pontuacao_areas))

print("\n")
print("=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")

print(f"\nMédia Temperatura: {media_temperatura:.2f}°C")
print(f"Média Comunicação: {media_comunicacao:.2f}%")
print(f"Média Bateria: {media_bateria:.2f}%")
print(f"Média Oxigênio: {media_oxigenio:.2f}%")
print(f"Média Estabilidade: {media_estabilidade:.2f}%")

print(f"\nCiclo mais crítico: {ciclo_critico}")
print(f"Maior risco: {maior_risco}")
print(f"Risco médio: {risco_medio:.2f}")
print(f"Ciclos críticos: {ciclos_criticos}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos_ciclos))

print("\nPontuação por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

print(f"\nÁrea mais afetada: {areas_monitoradas[indice_area]}")

print("\nClassificação Final:")

if risco_medio <= 2:
    print("MISSÃO ESTÁVEL")
elif risco_medio <= 5:
    print("MISSÃO EM ATENÇÃO")
else:
    print("MISSÃO CRÍTICA")

print("\nConclusão:")
print("A missão apresentou comportamento monitorado pelo sistema Mission Control AI.")
print("=" * 60)