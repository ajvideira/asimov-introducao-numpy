import numpy as np
import random

shape = (3, 5, 5)

tesouro = (
    random.randint(0, shape[0] - 1),
    random.randint(0, shape[1] - 1),
    random.randint(0, shape[2] - 1))

tabuleiro = np.zeros(shape, dtype=int)

print(tabuleiro)

def gerar_caminho_serpentina(andares, linhas, colunas):
    for andar in range(andares):
        faixa_colunas = range(colunas) if andar % 2 == 0 else range(colunas - 1, -1, -1)
        for coluna in faixa_colunas:
            faixa_linhas = range(linhas) if (andar + coluna) % 2 == 0 else range(linhas - 1, -1, -1)

            for linha in faixa_linhas:
                yield andar, linha, coluna

passos = 0
tesouro_encontrado = False

for posicao in gerar_caminho_serpentina(*shape):
    passos += 1
    tabuleiro[posicao] = 1
    print(f"Localização atual: {posicao}")

    if posicao == tesouro:
        print(f"Tesouro encontrado na posição {tesouro}")
        tesouro_encontrado = True
        break

if tesouro_encontrado:
    print(f"Total de passos necessários: {passos}")
else:
    print("Tesouro não encontrado após percorrer todo o tabuleiro.")