
dados_missao = [
    [27, 31, 35, 34, 39],
    [54, 48, 56, 89, 72],
    [88, 94, 30, 48, 75],
    [87, 96, 81, 99, 56],
    [19, 98, 76, 52, 15],
    [78, 98, 89, 45, 34]
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

Temperaturas = []
Comunicação = []
Bateria = []
Oxigenio = []
Estabilidade = []

pts_total_ciclo = []

num_ciclo = 0
ciclo_aux = 0
ciclo_critico = 0

print("===========================================\n")
print("MISSION CONTROL AI\n")
print("===========================================\n")
print("Missao: Alpha Century\n")
print("Equipe: FIAP COSMICA\n")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")
print("===========================================\n")

def verificar_temperatura(temperatura, indice_ciclo):
    if temperatura <= 18:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura muito baixa, risco de congelamento"
    elif temperatura > 18 and temperatura <= 30:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Temperatura estável"
    elif temperatura > 30 and temperatura <= 35:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Temperatura elevada"
    else:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Temperatura muito alta, risco de superaquecimento"

def verificar_comunicação(comunicacao, indice_ciclo):
    if comunicacao < 30:
        pts_ciclos[indice_ciclo].append(2)
        return "CRITICO | Comunicação com a base em nivel critico"
    elif comunicacao >= 30 and comunicacao < 60:
        pts_ciclos[indice_ciclo].append(1)
        return "ATENCAO | Comunicação instavel"
    else:
        pts_ciclos[indice_ciclo].append(0)
        return "NORMAL | Comunicação estavel"

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
        return "ATENCAO | Falta de oxigenio"
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
    Soma = sum(pts_ciclos[indice_ciclo])
    pts_total_ciclo.append(Soma)
    return Soma

def analisar_tendencia():
    if pts_total_ciclo[0] > pts_total_ciclo[-1]:
        return "A missão tem tendência a melhorar"
    elif pts_total_ciclo[0] < pts_total_ciclo[-1]:
        return "A missão tem tendência a piorar"
    else:
        return "A missão permaneceu estável em relação ao inicio"
        
for ciclo in dados_missao:
    ciclo_aux += 1
    print(f"CICLO: {ciclo_aux}\n")
    num_ciclo = 0
    for info in ciclo:
        if num_ciclo == 4:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_estabilidade(ciclo[num_ciclo], ciclo_aux - 1)}")
            Estabilidade.append(ciclo[num_ciclo])
        elif num_ciclo == 3:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_oxigenio(ciclo[num_ciclo], ciclo_aux - 1)}")
            Oxigenio.append(ciclo[num_ciclo])
        elif num_ciclo == 2:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_bateria(ciclo[num_ciclo], ciclo_aux - 1)}")
            Bateria.append(ciclo[num_ciclo])            
        elif num_ciclo == 1:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_comunicação(ciclo[num_ciclo], ciclo_aux - 1)}")
            Comunicação.append(ciclo[num_ciclo])
        else:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]} graus celsius | {verificar_temperatura(ciclo[num_ciclo],ciclo_aux - 1)}")
            Temperaturas.append(ciclo[num_ciclo])

        num_ciclo += 1
    print(f"Pontuacao de risco do ciclo: {risco_ciclo(ciclo_aux-1)}")
    print(classificar_ciclo(sum(pts_ciclos[ciclo_aux-1])))
    print(f"Recomendacoes:\n{gerar_recomendacoes(ciclo_aux - 1)}")
    print("---------------------------------------")

for qnt_cri in pts_total_ciclo:
    if qnt_cri > 5:
        ciclo_critico += 1
    else:
        ciclo_critico

media_temp = (sum(Temperaturas))/(len(Temperaturas))
media_comu = (sum(Comunicação))/(len(Comunicação))
media_bate = (sum(Bateria))/(len(Bateria))
media_oxi = (sum(Oxigenio))/(len(Oxigenio))
media_esta = (sum(Estabilidade))/(len(Estabilidade))


print("\n")
print("RELATORIO FINAL DA MISSAO\n")
print("\n")
print("---------------------------------------")

print("Missao: Alpha Century\n")
print("Equipe: FIAP COSMICA\n")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")



print(f"Media de temperatura: {round(media_temp,2)} graus celsius")
print(f"Media de comunicação: {round(media_comu,2)} %")
print(f"Media de bateria: {round(media_bate,2)} %")
print(f"Media de oxigênio: {round(media_oxi,2)} %")
print(f"Media de estabilidade: {round(media_esta,2)} %\n")

print(f"Ciclo mais critico: {pts_total_ciclo.index(max(pts_total_ciclo))+ 1}")
print(f"Maior pontuação de risco: {max(pts_total_ciclo)}")
print(f"Risco médio da missão: {round(sum(pts_total_ciclo)/len(pts_total_ciclo),2)}")
print(f"Quantidade de ciclos críticos: {ciclo_critico}\n")

print(f"Tendência da missão: {analisar_tendencia()}\n")

