def secuencia(inf, sup, sal):
    print(f"\nLa secuencia entre {inf} y {sup}, de {sal} en {sal}:")
    i =inf
    while i <= sup:
        print(i)
        i += sal

def main():
    inf = int(input("Ingrese Límite inferior: "))
    sup = int(input("Ingrese Límite superior: "))
    sal = int(input("Ingrese salto: "))
    secuencia(inf, sup, sal)
    
main()