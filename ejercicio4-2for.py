def secuencia(inf, sup, sal):
    print(f"\nLa secuencia entre {inf} y {sup}, de {sal} en {sal}:")
    for i in range(inf,sup+1,sal):
        print(i)

def main():
    inf = int(input("Ingrese Límite inferior: "))
    sup = int(input("Ingrese Límite superior: "))
    sal = int(input("Ingrese salto: "))
    secuencia(inf, sup, sal)
    
main()