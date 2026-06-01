
dados_missao = [
    [27, 31, 35, 34, 39],
    [32, 48, 56, 89, 72],
    [38, 94, 30, 48, 75],
    [41, 96, 81, 99, 56],
    [19, 98, 76, 52, 15],
    [36, 98, 89, 45, 34]
]

pts_ciclos = [
    [],
    [],
    [],
    [],
    [],
    []    
]

areas_monitoradas = [
    "Temperatura", "Comunicacao", "Bateria", "Oxigenio", "Estabilidade"
]

pts_areas_monitoradas = [
 "Temperatura interna",
 "Comunicacao com a base",
 "Sistema de energia",
 "Suporte de oxigenio",
 "Estabilidade operacional"
]

temperaturas = []
comunicacao_lista = []
bateria_lista = []
oxigenio_lista = []
estabilidade_lista = []

pts_total_ciclo = []
pts_total_atributos = []


num_ciclo = 0
ciclo_aux = 0
ciclo_critico = 0

print("==============================================================\n")
print("MISSION CONTROL AI\n")
print("==============================================================\n")
print("Missao: Alpha Century\n")
print("Equipe: FIAP COSMICA\n")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")
print("==============================================================\n")

def verificar_temperatura(temperatura, indice_ciclo):
    if temperatura <= 18:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura muito baixa, risco de congelamento"
    elif temperatura > 18 and temperatura <= 30:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Temperatura estavel"
    elif temperatura > 30 and temperatura <= 35:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura elevada"
    else:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Temperatura muito alta, risco de superaquecimento"

def verificar_comunicacao(comunicacao, indice_ciclo):
    if comunicacao < 30:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Comunicacao com a base em nivel critico"
    elif comunicacao >= 30 and comunicacao < 60:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Comunicacao instavel"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Comunicacao estavel"

def verificar_bateria(bateria, indice_ciclo):
    if bateria < 20:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Bateria em nivel critico"
    elif bateria >= 20 and bateria < 50:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Bateria abaixo do recomendado"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Bateria estavel"

def verificar_oxigenio(oxigenio, indice_ciclo):
    if oxigenio < 80:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Oxigenio em nivel critico"
    elif oxigenio >= 80 and oxigenio < 90:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Nivel de oxigenio abaixo do ideal"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Oxigenio estavel"
    
def verificar_estabilidade(estabilidade, indice_ciclo):
    if estabilidade < 40:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Estabilidade operacional critica"
    elif estabilidade >= 40 and estabilidade < 70:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Estabilidade operacional reduzida"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Estabilidade operacional adequada"

def classificar_ciclo(soma):
    if soma <=2:
        return "MISSAO ESTAVEL"
    elif soma > 2 and soma <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def gerar_recomendacoes(indice_ciclo):
    recomendacoes = {
        0: "Verificar controle termico",
        1: "Verificar sistemas de comunicacao",
        2: "Recarregar ou substituir bateria",
        3: "Verificar suprimento de oxigenio",
        4: "Verificar estabilidade operacional"
    }
    
    resultado = ""
    for area in range(len(areas_monitoradas)):
        if pts_ciclos[indice_ciclo][area] == 2:
            resultado += f"{recomendacoes[area]}\n"
        elif pts_ciclos[indice_ciclo][area] == 1:
            resultado += f"Monitorar {areas_monitoradas[area]} de perto\n"
    
    if resultado == "":
        return "Nenhuma acao necessaria\n"
    return resultado

def risco_ciclo(indice_ciclo):
    soma = sum(pts_ciclos[indice_ciclo])
    pts_total_ciclo.append(soma)
    return soma

def analisar_tendencia():
    if pts_total_ciclo[0] > pts_total_ciclo[-1]:
        return "A missao tem tendencia a melhorar"
    elif pts_total_ciclo[0] < pts_total_ciclo[-1]:
        return "A missao tem tendencia a piorar"
    else:
        return "A missão permaneceu estável em relação ao inicio"
    
def classificacao_final(soma_final):
    if soma_final >= 36:
        return "MISSAO CRITICA"
    elif soma_final < 36 and soma_final >= 18:
        return "MISSAO EM ATENÇAO"
    else:
        return "MISSAO ESTAVEL"

for ciclo in dados_missao:
    ciclo_aux += 1
    print(f"CICLO: {ciclo_aux}\n")

    num_ciclo = 0
    for info in ciclo:
        if num_ciclo == 4:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_estabilidade(ciclo[num_ciclo], ciclo_aux - 1)}")
            estabilidade_lista.append(ciclo[num_ciclo])
        elif num_ciclo == 3:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_oxigenio(ciclo[num_ciclo], ciclo_aux - 1)}")
            oxigenio_lista.append(ciclo[num_ciclo])
        elif num_ciclo == 2:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_bateria(ciclo[num_ciclo], ciclo_aux - 1)}")
            bateria_lista.append(ciclo[num_ciclo])            
        elif num_ciclo == 1:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_comunicacao(ciclo[num_ciclo], ciclo_aux - 1)}")
            comunicacao_lista.append(ciclo[num_ciclo])
        else:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]} graus celsius | {verificar_temperatura(ciclo[num_ciclo],ciclo_aux - 1)}")
            temperaturas.append(ciclo[num_ciclo])

        num_ciclo += 1

    print(f"\nPontuacao de risco do ciclo: {risco_ciclo(ciclo_aux-1)}")
    print(f"\n{classificar_ciclo(sum(pts_ciclos[ciclo_aux-1]))}")
    print(f"\nRecomendacoes:\n{gerar_recomendacoes(ciclo_aux - 1)}")
    print("-----------------------------------------------------------------------")

pts_atributos = list(map(list, zip(*pts_ciclos)))

for qnt_cri in pts_total_ciclo:
    if qnt_cri > 5:
        ciclo_critico += 1

media_temp = (sum(temperaturas))/(len(temperaturas))
media_comu = (sum(comunicacao_lista))/(len(comunicacao_lista))
media_bate = (sum(bateria_lista))/(len(bateria_lista))
media_oxi = (sum(oxigenio_lista))/(len(oxigenio_lista))
media_esta = (sum(estabilidade_lista))/(len(estabilidade_lista))

print("\n==============================================================\n")
print("RELATORIO FINAL DA MISSAO\n")
print("==============================================================\n")

print("Missao: Alpha Century\n")
print("Equipe: FIAP COSMICA\n")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")

print(f"Media de temperatura: {round(media_temp,2)} graus celsius")
print(f"Media de comunicação: {round(media_comu,2)} %")
print(f"Media de bateria: {round(media_bate,2)} %")
print(f"Media de oxigenio: {round(media_oxi,2)} %")
print(f"Media de estabilidade: {round(media_esta,2)} %\n")

print(f"Ciclo mais critico: {pts_total_ciclo.index(max(pts_total_ciclo))+ 1}")
print(f"Maior pontuacao de risco: {max(pts_total_ciclo)}")
print(f"Risco medio da missao: {round(sum(pts_total_ciclo)/len(pts_total_ciclo),2)}")
print(f"Quantidade de ciclos criticos: {ciclo_critico}\n")

print(f"Tendencia da missao: {analisar_tendencia()}\n")

print(f"Pontuacao acumulada por area:\n")

ciclo_aux = 0
for ciclo in range(len(pts_areas_monitoradas)):
    print(f"{pts_areas_monitoradas[ciclo_aux]}: {sum(pts_atributos[ciclo_aux])}")
    pts_total_atributos.append(sum(pts_atributos[ciclo_aux]))
    ciclo_aux += 1

print("\nArea mais afetada: ")
print(f"{pts_areas_monitoradas[pts_total_atributos.index(max(pts_total_atributos))]}\n")

soma_total = sum(pts_total_ciclo)
classificacao = classificacao_final(soma_total)

print("Classificacao final da missao:")
print(classificacao)

print("\nConclusao:")
if classificacao == "MISSAO CRITICA":
    print("A missao apresentou situacao critica durante a operacao. Multiplos sistemas estiveram em risco simultaneamente. E necessario acionar todos os protocolos de emergencia e priorizar o suporte a vida, energia e comunicacao.")
elif classificacao == "MISSAO EM ATENCAO":
    print("A missao apresentou instabilidade relevante durante a operacao. Apesar de não atingir estado critico, existem sistemas que requerem atencao continua. A equipe deve manter o plano de contingencia ativo e monitorar de perto as áreas afetadas.")
else:
    print("A missao transcorreu de forma estavel. Todos os sistemas operaram dentro dos limites esperados. Recomenda-se manter o monitoramento contínuo para garantir a estabilidade nas proximas fases da missao.")

print("\n==============================================================\n")