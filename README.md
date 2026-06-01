# Mission Control AI
### Sistema Inteligente de Monitoramento de Missão Espacial

**Missão:** Alpha Century  
**Equipe:** FIAP COSMICA  

**Integrantes:** Caio Henrique Ferraz da Silva RM:568992 e Leonardo Figueredo do Santos RM:573653

**Disciplina:** GS2026.1 — Pensamento Computacional e Automação com Python  

---

## Descrição do Projeto

O **Mission Control AI** é um sistema desenvolvido em Python que simula o monitoramento inteligente de uma missão espacial experimental. O sistema analisa dados de 6 ciclos de monitoramento, gera alertas automáticos, calcula o nível de risco de cada ciclo, identifica tendências e apresenta um relatório final completo no terminal.

---

## Estrutura do Repositório

```
mission-control-ai/
│
├── README.md
└── mission_control.py
```

---

## Como Executar

Nenhuma biblioteca externa é necessária. Basta ter o Python 3 instalado.

```bash
python3 mission_control.py
```

---

## Estrutura dos Dados

A matriz principal `dados_missao` contém 6 ciclos de monitoramento. Cada linha representa um ciclo e cada coluna representa uma informação monitorada, **nesta ordem**:

```
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

| Posição | Informação    | Unidade        |
|---------|---------------|----------------|
| 0       | Temperatura   | °C             |
| 1       | Comunicação   | %              |
| 2       | Bateria       | %              |
| 3       | Oxigênio      | %              |
| 4       | Estabilidade  | %              |

**Dados simulados utilizados:**

```python
dados_missao = [
    [27, 31, 35, 34, 39],  # Ciclo 1 - Inicio da missao
    [32, 48, 56, 89, 72],  # Ciclo 2 - Estabilizacao dos sistemas
    [38, 94, 30, 48, 75],  # Ciclo 3 - Queda parcial de oxigenio
    [41, 96, 81, 99, 56],  # Ciclo 4 - Alerta de temperatura
    [19, 98, 76, 52, 15],  # Ciclo 5 - Risco operacional
    [36, 98, 89, 45, 34]   # Ciclo 6 - Tentativa de recuperacao
]
```

---

## Regras de Alerta

Cada informação monitorada é classificada como **NORMAL**, **ATENCAO** ou **CRITICO** com base nas regras abaixo:

### Temperatura (°C)
| Condição               | Classificação |
|------------------------|---------------|
| ≤ 18°C                 | ATENCAO       |
| > 18°C e ≤ 30°C        | NORMAL        |
| > 30°C e ≤ 35°C        | ATENCAO       |
| > 35°C                 | CRITICO       |

### Comunicação (%)
| Condição        | Classificação |
|-----------------|---------------|
| < 30%           | CRITICO       |
| ≥ 30% e < 60%   | ATENCAO       |
| ≥ 60%           | NORMAL        |

### Bateria (%)
| Condição        | Classificação |
|-----------------|---------------|
| < 20%           | CRITICO       |
| ≥ 20% e < 50%   | ATENCAO       |
| ≥ 50%           | NORMAL        |

### Oxigênio (%)
| Condição        | Classificação |
|-----------------|---------------|
| < 80%           | CRITICO       |
| ≥ 80% e < 90%   | ATENCAO       |
| ≥ 90%           | NORMAL        |

### Estabilidade (%)
| Condição        | Classificação |
|-----------------|---------------|
| < 40%           | CRITICO       |
| ≥ 40% e < 70%   | ATENCAO       |
| ≥ 70%           | NORMAL        |

---

## Pontuação de Risco

Cada classificação gera uma pontuação de risco:

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENCAO       | 1      |
| CRITICO       | 2      |

Como cada ciclo possui 5 informações monitoradas, a **pontuação máxima por ciclo é 10 pontos**.

---

## Classificação do Ciclo

Após somar os pontos de risco do ciclo:

| Pontuação total | Classificação      |
|-----------------|--------------------|
| 0 a 2 pontos    | MISSAO ESTAVEL     |
| 3 a 5 pontos    | MISSAO EM ATENCAO  |
| 6 a 10 pontos   | MISSAO CRITICA     |

---

## Classificação Final da Missão

A classificação final é baseada na **soma acumulada de pontos de todos os ciclos** (pontuação máxima possível: 6 ciclos × 10 pontos = 60 pontos):

| Pontuação acumulada | Classificação Final  |
|---------------------|----------------------|
| ≥ 36 pontos         | MISSÃO CRÍTICA       |
| ≥ 18 e < 36 pontos  | MISSÃO EM ATENÇÃO    |
| < 18 pontos         | MISSÃO ESTÁVEL       |

> **Justificativa dos limiares:** 60 pontos é o máximo possível (6 ciclos × 10 pts). O limiar de 36 representa 60% do máximo, indicando que a maioria dos ciclos foi crítica. O limiar de 18 representa 30%, indicando que pelo menos parte relevante da missão apresentou problemas.

---

## Funções do Sistema

| Função                        | Descrição                                                              |
|-------------------------------|------------------------------------------------------------------------|
| `verificar_temperatura()`     | Classifica a temperatura e atribui pontuação ao ciclo                  |
| `verificar_comunicacao()`     | Classifica a comunicação e atribui pontuação ao ciclo                  |
| `verificar_bateria()`         | Classifica a bateria e atribui pontuação ao ciclo                      |
| `verificar_oxigenio()`        | Classifica o oxigênio e atribui pontuação ao ciclo                     |
| `verificar_estabilidade()`    | Classifica a estabilidade e atribui pontuação ao ciclo                 |
| `classificar_ciclo()`         | Retorna a classificação textual do ciclo com base na pontuação total   |
| `gerar_recomendacoes()`       | Gera recomendações automáticas baseadas nos alertas do ciclo           |
| `risco_ciclo()`               | Calcula e armazena a pontuação total de risco do ciclo                 |
| `analisar_tendencia()`        | Compara o primeiro e o último ciclo para indicar tendência da missão   |
| `classificacao_final()`       | Classifica a missão com base na pontuação acumulada de todos os ciclos |
