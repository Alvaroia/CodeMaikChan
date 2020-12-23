def collatz_step(numero):
    if numero % 2 == 0:
        numero = numero/2
    elif numero % 2 != 0 and numero != 1:
        numero = numero * 3 + 1

    return numero


def collazt_iter(numero):
    while numero != 1:
        resultado_iteracion = collatz_step(numero)
        print(resultado_iteracion)
        numero = resultado_iteracion


collazt_iter(27)


