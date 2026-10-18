from enum import Enum

import numpy as np
import random

class MODO(Enum):
    AVANCAR = 1
    RETROCEDER = 2

tamanho_tabuleiro = {
    "andares": 3,
    "linhas": 5,
    "colunas": 5
}

tabuleiro = np.zeros((tamanho_tabuleiro["andares"], tamanho_tabuleiro["linhas"], tamanho_tabuleiro["colunas"]), dtype=int)

tesouro = (
    random.randint(0, tamanho_tabuleiro["andares"]-1),
    random.randint(0, tamanho_tabuleiro["linhas"]-1),
    random.randint(0, tamanho_tabuleiro["colunas"]-1))

print(tabuleiro)

passos = 0

localizacao_atual = (0, 0, 0)

modo_linha = MODO.AVANCAR
modo_coluna = MODO.AVANCAR

while True:
    if passos == tabuleiro.size:
        print("Já percorreu tudo")
        break

    print(f"Localização atual: {localizacao_atual}")

    tabuleiro[localizacao_atual] = 1

    if localizacao_atual == tesouro:
        print(f"Tesouro encontrado na posição {tesouro}!")
        break

    ultimo_andar = localizacao_atual[0] == tabuleiro.shape[0] - 1
    ultima_linha = localizacao_atual[1] == tabuleiro.shape[1] - 1
    ultima_coluna = localizacao_atual[2] == tabuleiro.shape[2] - 1

    primeiro_andar = localizacao_atual[0] == 0
    primeira_linha = localizacao_atual[1] == 0
    primeira_coluna = localizacao_atual[2] == 0

    if (ultima_linha and ultima_coluna and modo_coluna == MODO.AVANCAR) or (not primeiro_andar and primeira_linha and primeira_coluna and modo_coluna == MODO.RETROCEDER):
        localizacao_atual = (localizacao_atual[0]+1, localizacao_atual[1], localizacao_atual[2])
        modo_linha = MODO.RETROCEDER if modo_linha == MODO.AVANCAR else MODO.AVANCAR
        modo_coluna = MODO.RETROCEDER if modo_coluna == MODO.AVANCAR else MODO.AVANCAR
    elif (ultima_linha and modo_linha == MODO.AVANCAR) or (primeira_linha and modo_linha == MODO.RETROCEDER):
        localizacao_atual = (localizacao_atual[0], localizacao_atual[1], localizacao_atual[2] + 1 if modo_coluna == MODO.AVANCAR else localizacao_atual[2] - 1)
        modo_linha = MODO.RETROCEDER if modo_linha == MODO.AVANCAR else MODO.AVANCAR
    else:
        localizacao_atual = (localizacao_atual[0], localizacao_atual[1] + 1 if modo_linha == MODO.AVANCAR else localizacao_atual[1] - 1, localizacao_atual[2])

    passos += 1

print(f"Total de passos necessários para encontrar o tesouro: {passos}")