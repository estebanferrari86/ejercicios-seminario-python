from random import randint 

def diferenciaSimetrica(lstA, lstB):
    res = [] + diferenciaAB(lstA, lstB) + diferenciaAB(lstB, lstA)
    return res

def diferenciaAB(lstA, lstB):
    res = []
    for num in lstA:
        if num not in lstB:
            res.append(num)
    return res
    
def interseccion (lstA, lstB):
    res = []
    for num in lstB:
        if num in lstA:
            res.append(num)
    return res

def union (lstA, lstB):
    res = [] + lstA
    for num in lstB:
        if num not in lstA:
            res.append(num)
    return res
    
def estaEnLista(num, lista):
    return num in lista

def cargarLista(lista, manual):
    if manual:
        num = int(input())
    else:
        num = randint(0,20)
    while num != 0:
        if num < 0:
            print("Error, número NO positivo.")
        elif estaEnLista(num, lista):
            print("Error, número repetido.")
        else:
            lista.append(num)
        if manual:
            num = int(input())
        else:
            num = randint(0,20)

def cargarConjuntos(lstA, lstB):
    tipoDeCarga = int(input("1. CARGA MANUAL\n2. CARGA AUTOMATICA\n"))
    cargarLista(lstA, tipoDeCarga == 1)
    cargarLista(lstB, tipoDeCarga == 1)
    
def verMenuYRetornarOpcion():
    print("1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMÉTRICA\n6. SALIR")
    opcion = int(input("Ingrese el valor de la opción:"))
    return opcion
    
def menu():
    opcion = verMenuYRetornarOpcion()
    lstA = []
    lstB = []
    while opcion != 6:
        if opcion == 1:
            cargarConjuntos(lstA, lstB)
            print("A: ", lstA)
            print("B: ", lstB)
        elif opcion == 2:
            print("A: ", lstA)
            print("B: ", lstB)
            print("union: ",union(lstA, lstB),"\n")
        elif opcion == 3:
            print("A: ", lstA)
            print("B: ", lstB)
            print("interseccion: ",interseccion(lstA, lstB),"\n")
        elif opcion == 4:
            print("A: ", lstA)
            print("B: ", lstB)
            print("diferencia A - B: ",diferenciaAB(lstA, lstB),"\n")
        elif opcion == 5:
            print("A: ", lstA)
            print("B: ", lstB)
            print("diferencia simetrica: ",diferenciaSimetrica(lstA, lstB),"\n")
        else:
            print("Debes elegir una opcion del 1 al 6\n")
        opcion = verMenuYRetornarOpcion()
    print("Adios!!")

def main():
    menu()

main()