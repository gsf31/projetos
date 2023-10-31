def soma_matrizes(m1, m2):
    # Verifica se as dimensões das matrizes são diferentes
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    
    resultado = []
    for i in range(len(m1)):
        linha_resultado = []
        for j in range(len(m1[0])):
            soma_elementos = m1[i][j] + m2[i][j]
            linha_resultado.append(soma_elementos)
        resultado.append(linha_resultado)
    
    return resultado
