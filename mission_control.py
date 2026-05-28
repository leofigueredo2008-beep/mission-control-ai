
dados_missao = [
    [27, 31, 35, 34, 39],
    [54, 48, 56, 89, 72],
    [88, 94, 30, 48, 75],
    [87, 96, 81, 99, 56],
    [19, 98, 76, 52, 15],
    [78, 98, 89, 45, 34]
]

pts_temp = []
pts_comu = []
pts_bate = []
pts_oxi = []
pts_esta = []


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

def verificar_temperatura(temperatura):
    if temperatura <= 18:
        return "ATENCAO"
    elif temperatura > 18 and temperatura <= 30:
        return "NORMAL"
    elif temperatura > 30 and temperatura <= 35:
        return "ATENCAO"
    else:
        return "CRITICO"




for ciclo in dados_missao:
    ciclo_aux += 1
    print("CICLO:", ciclo_aux)
    num_ciclo = 0
    for info in ciclo:
        if num_ciclo>=1:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]}%")
        else:
            print(f"{areas_monitoradas[num_ciclo]}: {ciclo[num_ciclo]} graus celsius", verificar_temperatura(ciclo[num_ciclo]))
        num_ciclo += 1
    print("---------------------------------------")