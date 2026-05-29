
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

num_ciclo = 0
ciclo_aux = 0

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
        return "CRITICO | Temperatura muito alta, ricos de superaquecimento"

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

for ciclo in dados_missao:
    ciclo_aux += 1
    print("CICLO:", ciclo_aux)
    num_ciclo = 0
    for info in ciclo:
        if num_ciclo == 4:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_estabilidade(ciclo[num_ciclo], ciclo_aux - 1)}")
        elif num_ciclo == 3:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_oxigenio(ciclo[num_ciclo], ciclo_aux - 1)}")
        elif num_ciclo == 2:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_bateria(ciclo[num_ciclo], ciclo_aux - 1)}")            
        elif num_ciclo == 1:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}% | {verificar_comunicação(ciclo[num_ciclo], ciclo_aux - 1)}")
        else:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]} graus celsius | {verificar_temperatura(ciclo[num_ciclo],ciclo_aux - 1)}")
        num_ciclo += 1
    print(f"Pontuacao de risco do ciclo: {sum(pts_ciclos[num_ciclo])}")
    print("---------------------------------------")




print(sum(pts_ciclos[num_ciclo]))








for cada_pontos in pts_ciclos:
    print(cada_pontos)