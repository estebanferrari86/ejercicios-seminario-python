def convertir(a):
    segundos = a % 60
    minParcial = a // 60
    minFinal = minParcial % 60
    horasParcial = minParcial // 60 
    horasFinal = horasParcial % 24
    dias = horasParcial // 24
    print("\n", dias, "dia(s),", horasFinal, "hora(s),", minFinal, "minuto(s),",segundos ,"segundo(s).")

def main():
     num= int(input("Ingrese el tirmpo en segundos: "))
     convertir(num)    

main()