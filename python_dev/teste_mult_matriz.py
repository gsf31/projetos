def sao_multiplicaveis(m1, m2):
    num_colunas_m1 = len(m1[0]) if m1 else 0  
    num_linhas_m2 = len(m2) if m2 else 0
    return num_colunas_m1 == num_linhas_m2

