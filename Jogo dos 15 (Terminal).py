'''
Algoritmo Jogo dos 15:
- Menu inicial com opções de dificuldade (fácil, médio, difícil).
    - Ná dificuldade fácil, o tabuleiro é embaralhado até 5 peças estarem fora do lugar.
    - Na dificuldade média, o tabuleiro é embaralhado até 10 peças estarem fora do lugar.
    - Na dificuldade difícil, o tabuleiro é embaralhado até 15 peças estarem fora do lugar.
- Gerar um tabuleiro 4x4 com os números de 1 a 15.
- Embaralhar os números, garantindo que use movimentos válidos.
- Exibir o tabuleiro no terminal.
- Permitir que o jogador mova os números usando as setas do teclado, garantindo que o movimento é válido.
- Verificar se o jogador venceu (os números estão em ordem de 1 a 15).
- Exibir mensagens de vitória ou derrota.
- Menu final com opções para jogar novamente ou sair. 
'''

import random
import os
import sys
import time
import keyboard

def gerar_tabuleiro():
    matriz = [[(i*4 + j + 1) for j in range(4)] for i in range(4)]
    matriz[3][3] = 0
    return matriz

def menu_inicial():
    print("Bem-vindo ao Jogo dos 15!")
    print("Escolha a dificuldade:")
    print("1. Fácil")
    print("2. Médio")
    print("3. Difícil")
    dificuldade = input("Digite o número da dificuldade: ")
    while (dificuldade != '1' and dificuldade != '2' and dificuldade != '3'):
        print("Opção inválida. Tente novamente.")
        dificuldade = input("Digite o número da dificuldade: ")
    return dificuldade

#A função de movimento deve mudar apenas o número 0 com os números adjacentes, garantindo que o movimento seja válido.
def movimento_cima(matriz):
    for coluna in range(4):
        for linha in range(1, 4):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna], matriz[linha-1][coluna] = matriz[linha-1][coluna], matriz[linha][coluna]
    time.sleep(0.2)
    exibir_tabuleiro(matriz)

def movimento_baixo(matriz):
    for coluna in range(4):
        for linha in range(2, -1, -1):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna], matriz[linha+1][coluna] = matriz[linha+1][coluna], matriz[linha][coluna]
    time.sleep(0.2) 
    exibir_tabuleiro(matriz)

def movimento_esquerda(matriz):
    for linha in range(4):
        for coluna in range(1, 4):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna], matriz[linha][coluna-1] = matriz[linha][coluna-1], matriz[linha][coluna]
    time.sleep(0.2)
    exibir_tabuleiro(matriz)

def movimento_direita(matriz):
    for linha in range(4):
        for coluna in range(2, -1, -1):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna], matriz[linha][coluna+1] = matriz[linha][coluna+1], matriz[linha][coluna]
    time.sleep(0.) 
    exibir_tabuleiro(matriz)

# A cada movimento, conferir quantas peças estão fora do lugar para determinar se o tabuleiro está embaralhado o suficiente
def embaralhar_tabuleiro(matriz, dificuldade):
    movimentos_feitos, movimentos_maximos, peças_a_mudar = 0, 250, [5, 10, 15]
    movimentos = [movimento_cima, movimento_baixo, movimento_esquerda, movimento_direita] 
    while peças_fora_do_lugar(matriz) < peças_a_mudar[int(dificuldade) - 1] and movimentos_feitos < movimentos_maximos:
        movimento = random.choice(movimentos)
        movimento(matriz)
        movimentos_feitos += 1

def peças_fora_do_lugar(matriz):
    contador = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] != 0 and matriz[i][j] != (i*4 + j + 1):
                contador += 1
    return contador

def exibir_tabuleiro(matriz):
    dificuldade_nome = ["Fácil", "Médio", "Difícil"]
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================")
    for i in range(4):
        print("     ", end="")
        for j in range(4):
            num = matriz[i][j]
            if num == 0:
            # O número 0 representa a peça vazia, que pode ser movida. Ele é exibido em cinza para diferenciá-lo dos outros números.
                print(" \033[1;30m 0 \033[m", end="")
            else:
                if matriz[i][j] != 0 and matriz[i][j] != (i*4 + j + 1):
                    print(f" \033[1;31m{num:2}\033[m ", end="")
                else:
                    print(f" \033[1;32m{num:2}\033[m ", end="")
        print()
    print("============================")

def verificar_vitoria(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] != 0 and matriz[i][j] != (i*4 + j + 1):
                return False
    return True

def menu_final():
    print("Parabéns! Você venceu!")
    print("Deseja jogar novamente?")
    print("1. Sim")
    print("2. Não")
    escolha = input("Digite o número da opção: ")
    while (escolha != '1' and escolha != '2'):
        print("Opção inválida. Tente novamente.")
        escolha = input("Digite o número da opção: ")
    return escolha == '1'

def main():
    jogando = True
    while jogando:
        matriz = gerar_tabuleiro()
        dificuldade = menu_inicial()
        embaralhar_tabuleiro(matriz, dificuldade)
        exibir_tabuleiro(matriz)

        while jogando:
            tecla = keyboard.read_key(suppress=True)
            if tecla == 'up':
                movimento_cima(matriz)
            elif tecla == 'down':
                movimento_baixo(matriz)
            elif tecla == 'left':
                movimento_esquerda(matriz)
            elif tecla == 'right':
                movimento_direita(matriz)
            else:
                continue

            if verificar_vitoria(matriz):
                exibir_tabuleiro(matriz)
                if not menu_final():
                    jogando = False
                break

main()

    
        
    


