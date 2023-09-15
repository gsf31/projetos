def maximo(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > y and  z > x:
        return z
    if x == y == z:
        return x