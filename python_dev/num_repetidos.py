num = input("Digite um número inteiro: ")
tem_adjacente = False

i = 0
while i < len(num) - 1:
    if num[i] == num[i+1]:
        tem_adjacente = True
        break
    i += 1

if tem_adjacente:
    print("sim")
else:
    print("não")