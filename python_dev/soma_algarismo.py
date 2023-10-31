numero = int(input("Digite um número: "))

soma = 0

while numero > 0:
    ultimo_digito = numero % 10
    soma = soma + ultimo_digito
    numero = numero // 10
print(soma)
