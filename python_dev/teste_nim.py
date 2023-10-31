def computador_escolhe_jogada(n, m):
    computador_remove_peca = 1

    while computador_remove_peca != m:
        if (n - computador_remove_peca) % (m + 1) == 0:
            return computador_remove_peca

        else:
            computador_remove_peca += 1

        return computador_remove_peca

def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogava_valida:
        jogador_remove = int(input("Quantas peças você vai tirar? "))
        if jogador_remove > m or jogador_remove < 1:

            print("Epa! Jogada inválida! Tente de novo.")

        else:
            jogada_valida = True

    return jogador_remove


            
