def factorial(n):
    """ Calcula el factorial de n.

    n in > 0
    returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input('Escribe un entero: '))
print(factorial(n))
a = True
b = False
print(a and b)
