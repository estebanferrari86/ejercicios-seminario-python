def comparar(a,b,c):
    if (a > c):
        if (b < c):
            mismaDistancia = (a-c == c-b)
        else:
            mismaDistancia = (a-b == b-c)
    elif (a == c or b ==c):
        mismaDistancia = False
    else:
        mismaDistancia = (c-a == a-b)
    return mismaDistancia

def comprobarDistacia(a, b, c):
    if (a > b):
        mismaDistancia = comparar(a,b,c)
    elif (a == b):
        mismaDistancia = (a == c)
    else:
        mismaDistancia = comparar(b,a,c)
    return mismaDistancia

def main():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    if comprobarDistacia(a, b, c):
        print("\nEstán igualmente distanciados!")
    else:
        print("\nNO Están igualmente distaciados!")

main()
