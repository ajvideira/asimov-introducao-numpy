import os

import numpy as np

def imprimir_tabuleiro(tabuleiro: np.ndarray) -> None:
    linhas = [" " + " | ".join(linha) for linha in tabuleiro]
    print("\n---+---+---\n".join(linhas))

def verificar_vitoria(tabuleiro: np.ndarray, jogador) -> bool:
    casas = tabuleiro == jogador

    return (
        casas.all(axis=1).any()
        or casas.all(axis=0).any()
        or casas.diagonal().all()
        or np.fliplr(casas).diagonal().all()
    )

def fazer_jogada(tabuleiro: np.ndarray, jogador: str):
    while True:
        posicao = input(f"Jogador {jogador}, escolha uma posição: ").strip()
        posicoes = np.argwhere(tabuleiro == posicao)

        if len(posicoes) != 1 or posicao not in "123456789":
            print("Posição inválida.")
            continue

        linha, coluna = posicoes[0]
        tabuleiro[linha][coluna] = jogador
        break

def main():
    tabuleiro = np.arange(1, 10).reshape((3, 3)).astype(str)
    imprimir_tabuleiro(tabuleiro)

    for turno in range(1,10):
        jogador = "X" if turno % 2 == 0 else "O"
        try:
            fazer_jogada(tabuleiro, jogador)
        except EOFError:
            print("\nPartida encerrada")
            return

        if os.environ.get("TERM"):
            os.system("clear")

        imprimir_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador):
            print(f"Jogador {jogador} venceu!")
            break
        elif turno == 9:
            print("Deu empate!")

if __name__ == "__main__":
    main()