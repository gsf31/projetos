def primo(numero):
    
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


def maior_primo(numero):
    
    while numero >= 2:
        if primo(numero):
            return numero
        numero -= 1

    return None

