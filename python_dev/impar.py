n = int(input("Digite um número inteiro positivo: "))
i = 0
num = 1

while i <= n:
    if num % 2 == 1:
        print(num)
        i = i + 1
    num = num + 1