import math

# leia as coordenadas x e y do primeiro ponto
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))

# leia as coordenadas x e y do segundo ponto
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# calcule a distância entre os dois pontos usando a fórmula da distância euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# imprima a distância entre os dois pontos
print("A distância entre os pontos ({}, {}) e ({}, {}) é {:.2f}".format(x1, y1, x2, y2, distancia))