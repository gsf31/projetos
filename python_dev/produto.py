tamanho = int(input("Digite a quantidade de números para essa sequência de multiplicações: "))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1
print("A soma dos valores é igual a", produto)