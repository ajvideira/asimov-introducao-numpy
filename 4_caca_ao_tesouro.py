import os

import numpy as np
import random

def gerar_caminho_serpentina(andares, linhas, colunas):
    for andar in range(andares):
        faixa_colunas = range(colunas) if andar % 2 == 0 else range(colunas - 1, -1, -1)
        for coluna in faixa_colunas:
            faixa_linhas = range(linhas) if (andar + coluna) % 2 == 0 else range(linhas - 1, -1, -1)

            for linha in faixa_linhas:
                yield andar, linha, coluna

def imprimir_titulo() -> None:
    print("Caça ao Tesouro v1.0")

def imprimir_modo_jogo():
    print("1-Jogo automático (Máquina joga)")
    print("2-Jogo manual (Jogador joga)")

def iniciar_parametros():
    iniciar_tabuleiro()
    posicionar_tesouro()

def iniciar_tabuleiro():
    print("Iniciando tabuleiro...")

    global shape, tabuleiro

    eixo_x = ler_inteiro("Eixo X (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    eixo_y = ler_inteiro("Eixo Y (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    eixo_z = ler_inteiro("Eixo Z (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    shape = (eixo_x, eixo_y, eixo_z)

    tabuleiro = np.zeros(shape, dtype=int)

def posicionar_tesouro():
    print("Posicionando tesouro...")

    global tesouro

    while True:
        tesouro = (
            random.randint(0, shape[0] - 1),
            random.randint(0, shape[1] - 1),
            random.randint(0, shape[2] - 1)
        )

        if tesouro != (0, 0, 0):
            break

def ler_inteiro(mensagem: str, valores_permitidos: list[int]) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor not in valores_permitidos:
                raise ValueError
            return valor
        except ValueError:
            print("Valor inválido")

def imprimir_menu_navegacao() -> None:
    print("Controle de Navegação")
    print("A - Esquerda")
    print("D - Direita")
    print("W - Cima")
    print("S - Baixo")
    print("Z - Descer de andar")
    print("X - Subir de andar")

def escolher_proxima_posicao(posicao_anterior: tuple[int, int, int]) -> tuple[int, int, int]:
    while True:
        try:
            posicao = input("Escolha: ")

            print(str.upper(posicao))

            if str.upper(posicao) == "A":
                if posicao_anterior[2] == 0:
                    raise ValueError
                else:
                    return posicao_anterior[0], posicao_anterior[1], posicao_anterior[2]-1
            elif str.upper(posicao) == "D":
                if posicao_anterior[2] == shape[2] - 1:
                    raise ValueError
                else:
                    return posicao_anterior[0], posicao_anterior[1], posicao_anterior[2]+1
            elif str.upper(posicao) == "W":
                if posicao_anterior[1] == 0:
                    raise ValueError
                else:
                    return posicao_anterior[0], posicao_anterior[1]-1, posicao_anterior[2]
            elif str.upper(posicao) == "S":
                if posicao_anterior[1] == shape[1] - 1:
                    raise ValueError
                else:
                    return posicao_anterior[0], posicao_anterior[1]+1, posicao_anterior[2]
            elif str.upper(posicao) == "Z":
                if posicao_anterior[0] == 0:
                    raise ValueError
                else:
                    return posicao_anterior[0]-1, posicao_anterior[1], posicao_anterior[2]
            elif str.upper(posicao) == "X":
                if posicao_anterior[0] == shape[0] - 1:
                    raise ValueError
                else:
                    return posicao_anterior[0]+1, posicao_anterior[1], posicao_anterior[2]
            else:
                raise ValueError
        except ValueError:
            print("Comando inválido")

shape: tuple[int, int, int]
tabuleiro: np.ndarray
tesouro: tuple[int, int, int]

imprimir_titulo()
iniciar_parametros()

imprimir_modo_jogo()
opcao = ler_inteiro("Escolha sua opção (1,2): ", [1,2])

passos = 0
posicao_anterior = (0,0,0)

if opcao == 1:

    for posicao in gerar_caminho_serpentina(*shape):
        tabuleiro[posicao_anterior] = 0
        tabuleiro[posicao] = 1
        posicao_anterior = posicao
        print(f"Localização atual: {posicao}")
        print(tabuleiro)

        if posicao == tesouro:
            print(f"Tesouro encontrado na posição {tesouro}")
            tesouro_encontrado = True
            break

        passos += 1
else:
    while True:
        os.system("clear")
        tabuleiro[posicao_anterior] = 1
        print(tabuleiro)

        if posicao_anterior == tesouro:
            break

        passos += 1

        if posicao_anterior == tesouro:
            break

        imprimir_menu_navegacao()
        posicao = escolher_proxima_posicao(posicao_anterior)

        tabuleiro[posicao_anterior] = 0
        posicao_anterior = posicao


print(f"Total de passos necessários: {passos}")

##shape = (1, 5, 5)
##
##tesouro = (
##    random.randint(0, shape[0] - 1),
##    random.randint(0, shape[1] - 1),
##    random.randint(0, shape[2] - 1))
##
##tabuleiro = np.zeros(shape, dtype=int)
##
##print(tabuleiro)
##
##passos = 0
##tesouro_encontrado = False
##
##for posicao in gerar_caminho_serpentina(*shape):
##    passos += 1
##    tabuleiro[posicao] = 1
##    print(f"Localização atual: {posicao}")
##
##    if posicao == tesouro:
##        print(f"Tesouro encontrado na posição {tesouro}")
##        tesouro_encontrado = True
##        break
##
##if tesouro_encontrado:
##    print(f"Total de passos necessários: {passos}")
##else:
##    print("Tesouro não encontrado após percorrer todo o tabuleiro.")