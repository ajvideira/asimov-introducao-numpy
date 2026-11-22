import random
import os

import numpy as np

MOVIMENTOS = {
    "A": (0, 0, -1),
    "D": (0, 0, 1),
    "W": (0, -1, 0),
    "S": (0, 1, 0),
    "Z": (-1, 0, 0),
    "X": (1, 0, 0),
}

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

def definir_shape() -> tuple[int, int, int]:
    print("Definindo shape...")
    while True:
        andares = ler_inteiro("Andares (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        linhas = ler_inteiro("Linhas (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        colunas = ler_inteiro("Colunas (1-10): ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        if andares == linhas == colunas == 1:
            print("O tabuleiro não pode ser 1x1x1. Configure novamente.")
        else:
            return andares, linhas, colunas

def criar_tabuleiro(shape: tuple[int, int, int]) -> np.ndarray:
    print("Criando tabuleiro...")

    return np.zeros(shape, dtype=int)

def posicionar_tesouro(shape: tuple[int, int, int]) -> tuple[int, int, int]:
    print("Posicionando tesouro...")

    if shape == (1, 1, 1):
        raise ValueError("O tabuleiro não pode ser 1x1x1")

    while True:
        andar = random.randint(0, shape[0] - 1)
        linha = random.randint(0, shape[1] - 1)
        coluna = random.randint(0, shape[2] - 1)

        if (andar, linha, coluna) != (0, 0, 0):
            break
    return andar, linha, coluna

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

def escolher_proxima_posicao(posicao_anterior: tuple[int, int, int], shape: tuple[int, int, int]) -> tuple[int, int, int]:
    andar, linha, coluna = posicao_anterior
    andares, linhas, colunas = shape

    while True:
        comando = input("Escolha: ").strip().upper()
        deslocamento = MOVIMENTOS.get(comando)

        if deslocamento is None:
            print("Comando inválido.")
            continue

        delta_andar, delta_linha, delta_coluna = deslocamento

        novo_andar = andar + delta_andar
        nova_linha = linha + delta_linha
        nova_coluna = coluna + delta_coluna

        if (
            0 <= novo_andar < andares
            and 0 <= nova_linha < linhas
            and 0 <= nova_coluna < colunas
        ):
            return novo_andar, nova_linha, nova_coluna
        else:
            print("Movimento sai do tabuleiro.")

def main() -> None:
    imprimir_titulo()

    shape: tuple[int, int, int] = definir_shape()
    tabuleiro: np.ndarray = criar_tabuleiro(shape)
    tesouro: tuple[int, int, int] = posicionar_tesouro(shape)

    imprimir_modo_jogo()
    opcao = ler_inteiro("Escolha sua opção (1,2): ", [1, 2])

    passos = 0
    posicao_anterior = (0, 0, 0)

    if opcao == 1:
        for posicao in gerar_caminho_serpentina(*shape):
            tabuleiro[posicao_anterior] = 0
            tabuleiro[posicao] = 1
            posicao_anterior = posicao
            print(f"Localização atual: {posicao}")
            print(tabuleiro)

            if posicao == tesouro:
                print(f"Tesouro encontrado na posição {tesouro}")
                break

            passos += 1
    else:
        while True:
            if os.environ.get("TERM"):
                os.system("clear")

            tabuleiro[posicao_anterior] = 1
            print(tabuleiro)

            if posicao_anterior == tesouro:
                print(f"Tesouro encontrado na posição {tesouro}")
                break

            imprimir_menu_navegacao()
            posicao = escolher_proxima_posicao(posicao_anterior, shape)

            tabuleiro[posicao_anterior] = 0
            posicao_anterior = posicao

            passos += 1

    print(f"Total de passos necessários: {passos}")

if __name__ == "__main__":
    main()