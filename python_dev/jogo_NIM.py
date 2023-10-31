def computador_escolhe_jogada(n, m):
    
    jogada = n % (m + 1)
    if jogada == 0 or jogada > m:
        jogada = m
    return jogada


def usuario_escolhe_jogada(n, m):
    
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada > m:
            print("Oops! Jogada inválida! Tente de novo.")
            jogada = 0
    return jogada


def partida():
    
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    tipo_jogo = int(input("2 - para jogar um campeonato "))

    if tipo_jogo == 1:
        print("Você escolheu uma partida isolada!")
        print()
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        print()

        if n % (m + 1) == 0:
            print("Você começa!")
            vez_do_usuario = True
        else:
            print("Computador começa!")
            vez_do_usuario = False

        while n > 0:
            if vez_do_usuario:
                jogada = usuario_escolhe_jogada(n, m)
                vez_do_usuario = False
                print("Você tirou", jogada, "peça(s).")
            else:
                jogada = computador_escolhe_jogada(n, m)
                vez_do_usuario = True
                print("O computador tirou", jogada, "peça")
import random

def play_nim():
    print("Bem-vindo ao jogo do NIM!")
    print("O objetivo do jogo é não ficar com a última peça.")
    
    num_peças = random.randint(10, 30)
    print("Existem", num_peças, "peças no tabuleiro.")
        
    jogador_começa = random.choice([True, False])
    if jogador_começa:
        print("Você começa jogando!")
    else:
        print("O computador começa jogando!")
    
    # Loop principal do jogo
    while num_peças > 0:
        if jogador_começa:
            # Turno do jogador
            jogada_válida = False
            while not jogada_válida:
                jogada = input("Quantas peças você quer remover? ")
                if not jogada.isdigit():
                    print("Por favor, digite um número inteiro positivo.")
                elif int(jogada) < 1 or int(jogada) > min(num_peças, 3):
                    print("Por favor, escolha um número entre 1 e", min(num_peças, 3),".")
                else:
                    jogada_válida = True
            
            num_peças -= int(jogada)
            print("Você removeu", jogada, "peças. Restam", num_peças, "peças no tabuleiro.")          
            # Verificar se o jogador venceu
            if num_peças == 0:
                print("Parabéns, você venceu!")
                return
        else:
            # Turno do computador
            jogada = random.randint(1, min(num_peças, 3))
            num_peças -= jogada
            print("O computador removeu", jogada, "peças. Restam", num_peças, "peças no tabuleiro.")         
            # Verificar se o computador venceu
            if num_peças == 0:
                print("O computador venceu! Tente novamente.")
                return
        
        # Alternar entre jogador e computador
        jogador_começa = not jogador_começa

play_nim()
