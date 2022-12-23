def condicion(num,par):
    res = num%2 == par
    if (par == 2):
        res = True
    return res

def secuencia(inf, sup, sal, par):
    if (par == 0):
        palabra = "par"
    elif (par == 1):
        palabra = "impar" 
    else:
        palabra = "ambos"
    print(f"\nLa secuencia entre {inf} y {sup}, de {sal} en {sal} y {palabra} es:")
    i =inf
    while i <= sup:
        if condicion(i,par):
            print(i)
        i += sal

def main():
    inf = int(input("Ingrese Límite inferior: "))
    sup = int(input("Ingrese Límite superior: "))
    sal = int(input("Ingrese salto: "))
    par = int(input('Ingrese paridad -> "0 (par), 1 (impar), 2 (ambos)": '))
    secuencia(inf, sup, sal, par)
    
main()