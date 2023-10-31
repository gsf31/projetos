tamanho = int(input("Digite a quantidade de números para essa sequência de somatória: "))

soma = 0
valor = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    i = i + 1
print("A soma dos valores é igual a", soma)