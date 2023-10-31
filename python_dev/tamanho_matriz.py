def dimensoes(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0]) if matriz else 0  # Verifica o tamanho da primeira linha, caso a matriz não seja vazia
    
    print(f"{num_linhas}X{num_colunas}")
