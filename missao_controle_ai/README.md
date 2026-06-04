# Mission Control AI

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python para a Global Solution da disciplina **Pensamento Computacional e Automação com Python (FIAP)**.

## Sobre o Projeto

O **Mission Control AI** simula o monitoramento de uma missão espacial experimental por meio da análise de diferentes ciclos operacionais.

O sistema acompanha indicadores críticos da missão e realiza análises automáticas para identificar riscos, gerar alertas, classificar o estado da missão e apresentar recomendações para a equipe de controle.

---

## Objetivos

O sistema é capaz de:

* Monitorar dados simulados da missão espacial;
* Avaliar múltiplos ciclos de operação;
* Gerar alertas automáticos;
* Calcular níveis de risco;
* Classificar cada ciclo da missão;
* Identificar tendências de melhora ou piora;
* Determinar a área mais afetada da operação;
* Gerar recomendações automáticas;
* Exibir um relatório final completo.

---

## Informações Monitoradas

Cada ciclo da missão possui os seguintes indicadores:

| Indicador    | Descrição                                 |
| ------------ | ----------------------------------------- |
| Temperatura  | Temperatura interna do módulo (°C)        |
| Comunicação  | Qualidade do sinal com a base (%)         |
| Bateria      | Nível de energia disponível (%)           |
| Oxigênio     | Disponibilidade de oxigênio (%)           |
| Estabilidade | Estabilidade operacional dos sistemas (%) |

---

## Estrutura dos Dados

A missão é representada por uma matriz chamada `dados_missao`.

Exemplo:

```python
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]
```

Cada linha representa um ciclo da missão:

```python
[
 temperatura,
 comunicacao,
 bateria,
 oxigenio,
 estabilidade
]
```

---

## Regras de Classificação

### Temperatura

| Condição      | Status  |
| ------------- | ------- |
| < 18°C        | ATENÇÃO |
| 18°C até 30°C | NORMAL  |
| 31°C até 35°C | ATENÇÃO |
| > 35°C        | CRÍTICO |

### Comunicação

| Condição    | Status  |
| ----------- | ------- |
| < 30%       | CRÍTICO |
| 30% até 59% | ATENÇÃO |
| ≥ 60%       | NORMAL  |

### Bateria

| Condição    | Status  |
| ----------- | ------- |
| < 20%       | CRÍTICO |
| 20% até 49% | ATENÇÃO |
| ≥ 50%       | NORMAL  |

### Oxigênio

| Condição    | Status  |
| ----------- | ------- |
| < 80%       | CRÍTICO |
| 80% até 89% | ATENÇÃO |
| ≥ 90%       | NORMAL  |

### Estabilidade

| Condição    | Status  |
| ----------- | ------- |
| < 40%       | CRÍTICO |
| 40% até 69% | ATENÇÃO |
| ≥ 70%       | NORMAL  |

---

## Sistema de Pontuação

Cada status gera uma pontuação de risco:

| Status  | Pontos |
| ------- | ------ |
| NORMAL  | 0      |
| ATENÇÃO | 1      |
| CRÍTICO | 2      |

Pontuação máxima por ciclo:

```text
5 indicadores × 2 pontos = 10 pontos
```

---

## Classificação da Missão

| Pontuação | Classificação     |
| --------- | ----------------- |
| 0 a 2     | MISSÃO ESTÁVEL    |
| 3 a 5     | MISSÃO EM ATENÇÃO |
| 6 a 10    | MISSÃO CRÍTICA    |

---

## Funcionalidades Implementadas

* Análise automática de temperatura
* Análise automática de comunicação
* Análise automática de bateria
* Análise automática de oxigênio
* Análise automática de estabilidade
* Classificação por ciclo
* Cálculo de risco
* Tendência da missão
* Identificação da área mais afetada
* Relatório final detalhado

---

## Tecnologias Utilizadas

* Python 3
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for`)
* Listas
* Matrizes
* Funções
* Manipulação de dados

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/mission-control-ai.git
```

Acesse a pasta:

```bash
cd mission-control-ai
```

Execute o programa:

```bash
python mission_control.py
```

---

## Estrutura do Projeto

```text
mission-control-ai/
│
├── mission_control.py
├── README.md
└── assets/
    ├── missao_controle_ia.drawio.png
    └── execucao.png
```

---

## Equipe

**Nome da Missão:** Orion Nexus

**Equipe:** Equipe NextBand

### Integrantes

| Nome                                  | RM     |
| ------------------------------------- | ------ |
| Mateus de Oliveira Fernandes Neves    | 572431 |
| Marcelo do Nascimento Batista Pereira | 569410 |
| Nathan Hiroshi Watanabe               | 572806 |
