def validar(inf,sup,val):
    return (val >= inf and val <= sup)
    
def comprobar(inf,sup,texto):
    val = int(input(texto))
    while not validar(inf,sup,val):
        val = int(input(f"Error ingrese el valor [{inf}-{sup}]:"))
    return val

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
    for i in range(inf,sup+1,sal):
        if condicion(i,par):
            print(i)
        

def main():
    inf = comprobar(1,100,"Ingrese Límite inferior: ")
    sup = comprobar(1,100,"Ingrese Límite superior: ")
    sal = int(input(f"Ingrese salto: "))
    par = comprobar(0,2,'Ingrese paridad -> "0 (par), 1 (impar), 2 (ambos)": ')
    secuencia(inf, sup, sal, par)
    
main()