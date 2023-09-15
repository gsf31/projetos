num = int(input("Digite um número inteiro positivo: "))

if num <= 1:
    print("não primo")
else:
    i = 2
    primo = True
    while i <= num**0.5:
        if num % i == 0:
            primo = False
            break
        i = i + 1
    if primo:
        print("primo")
    else:
        print("não primo")

