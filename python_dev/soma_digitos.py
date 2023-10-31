# Pede ao usuário para digitar um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a soma dos dígitos com zero (elemento neutro da soma)
soma = 0

# Enquanto houver dígitos no número
while numero > 0:
    # Calcule o último dígito do número usando o operador %
    ultimo_digito = numero % 10
    # Adiciona o último dígito à soma
    soma = soma + ultimo_digito
    # Remove o último dígito do número usando o operador //
    numero = numero // 10

# Exibe a soma dos dígitos
print("A soma dos dígitos é:", soma)




