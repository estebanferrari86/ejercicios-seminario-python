def esPositivoONegativo(num):
    if num < 0:
        msj = "negativo"
    elif num > 0:
        msj = "positivo"
    else:
        msj = "cero"
    return msj

def esEnteroNaturalOReal(num):
    esEntero = "." not in str(num) or (str(num).index(".") + 2 == len(str(num)) and str(num)[-1] == "0")
    if esEntero:
        msj = "entero"
        if num > 0:
            msj = "entero natural"
    else:
        msj = "real"
    return msj

def main():
    num = float(input("Ingrese un número: "))
    msjNoR = esEnteroNaturalOReal(num)
    msjPoN = esPositivoONegativo(num)
    print(f"\nEl número es {msjPoN} y {msjNoR}.")
    
main()