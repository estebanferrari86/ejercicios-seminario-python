import math

def areaCirc(radio):
    area = math.pi * (radio * radio)
    return area

def areaCuad(lado):
    return lado * lado

def areaNegra(lado):
    diametroDelCirculoGrande = lado / 3 * 2
    diametroDelCirculoChico = lado / 3
    areaCircGrande = areaCirc(diametroDelCirculoGrande /2)
    areaCircChico = areaCirc(diametroDelCirculoChico /2)
    areaCuadrado = areaCuad(lado)
    areaNegra = areaCuadrado - areaCircGrande - (areaCircChico * 2)
    return areaNegra

def main():
    ladoDelcuadrado = float(input("Ingrese el lado: "))
    area = areaNegra(ladoDelcuadrado)
    areaCuadrado = areaCuad(ladoDelcuadrado)
    porcentaje = (area*100) / areaCuadrado
    print(f"\nEl area negra es {round(area,2)} y es un {round(porcentaje,2)}% del area total del cuadrado")
    
main()