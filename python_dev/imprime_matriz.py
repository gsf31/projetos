def imprime_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    for i in range(num_linhas):
        for j in range(num_colunas):
            print(matriz[i][j], end="")
            if j < num_colunas - 1:
                print(" ", end="")
        print()  # Adiciona uma nova linha após cada linha da matriz


        
        
