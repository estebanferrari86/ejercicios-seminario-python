def bono(sueldoBase):
    bono = sueldoBase * 0.2
    if (sueldoBase > 2000):
        bono = sueldoBase * 0.15
    return bono

def plusH(sueldoBase, tieneHijos):
    plus = 0
    if tieneHijos:
        plus = sueldoBase * 0.05
    return plus

def plusC(sueldoBase, categoria):
    if ( categoria > 0 and categoria <=3):
        plus = sueldoBase * 0.1
    elif ( categoria > 3 and categoria <=6):
        plus = sueldoBase * 0.12
    else:
        plus = sueldoBase * 0.2
    return plus

def plus(sueldoBase, tieneHijos, categoria):
    if (categoria > 6 and categoria <= 9) and tieneHijos:
        tieneHijos = False
    plusHijos = plusH(sueldoBase, tieneHijos)
    plusCategoria = plusC(sueldoBase, categoria)
    return plusHijos + plusCategoria

def main():
    sueldoBase = float(input("Ingerse el sueldo Base: "))
    tieneHijosSoN = input("Tiene hijos (s/n)?: ")
    categoria = int(input("Ingrese categoria (1 - 9): "))
    if ( tieneHijosSoN == "s"):
        tieneHijos = True
    else:
        tieneHijos = False
    total = sueldoBase + bono(sueldoBase) + plus(sueldoBase, tieneHijos, categoria)
    print(f"\nEl sueldo total será de ${total}")
    