def criar_matriz():
    # Solicita o número de linhas e colunas da matriz
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))

    # Inicializa a matriz como uma lista de listas
    matriz = []
    
    # Preenche a matriz com os elementos digitados pelo usuário
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): "))
            linha.append(elemento)
        matriz.append(linha)

    return matriz

def imprimir_matriz(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    print("Matriz:")
    for i in range(num_linhas):
        for j in range(num_colunas):
            # Imprime cada elemento da matriz com duas casas decimais e separados por tabulação
            print(f"{matriz[i][j]}", end=" ")  
        # Imprime uma quebra de linha após cada linha da matriz
        print()

# Chama a função para criar a matriz
matriz_original = criar_matriz()

# Chama a função para imprimir a matriz no formato vertical
imprimir_matriz(matriz_original)
