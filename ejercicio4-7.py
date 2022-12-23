
def dibujarA(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if True:
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarB(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f==b-1 or c==0 or f==0 or c==b-1:
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarC(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f<=c:
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarD(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if (f+c<=b-1 and f<=c) or (f+c>=b-1 and f>=c):
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarE(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if (f+c>=b-1 and f>=c) or f== b//2 or c== b//2:
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarF(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f==c or f==0 or f+c==b-1 or f==b-1:
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarG(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)==c or f-(b//2)==c or f+c-(b//2)==b-1 or f+c+(b//2)==b-1 :
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()
        
def dibujarH(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)>=c and f-(b//2)<=c and f+c-(b//2)<=b-1 and f+c+(b//2)>=b-1 :
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def dibujarI(b,car,esp):
    for f in range (0,b):
        for c in range(0,b):
            if f+(b//2)<=c or f-(b//2)>=c or f+c-(b//2)>=b-1 or f+c+(b//2)<=b-1 :
                print(car,end=" ")
            else:
                print(esp,end=" ")
        print()

def comprobarB(texto):
    b = int(input(texto))
    while (b < 5 or b%2==0):
        b = int(input(texto))
    return b

def comprobarCarYEsp(texto, carDeComparacion,error):
    ingreso = input(texto)
    while ( ingreso == carDeComparacion):
        ingreso = input(error)
    return ingreso

def dibujar(b,car,esp):
    figura = input("Ingrese la figura que desea que se imprima (A-I): ")
    print("\n\n")
    if figura=="A" or figura=="a":
        dibujarA(b,car,esp)
    elif figura=="B" or figura=="b":
        dibujarB(b,car,esp)
    elif figura=="C" or figura=="c":
        dibujarC(b,car,esp)
    elif figura=="D" or figura=="d":
        dibujarD(b,car,esp)
    elif figura=="E" or figura=="e":
        dibujarE(b,car,esp)
    elif figura=="F" or figura=="f":
        dibujarF(b,car,esp)
    elif figura=="G" or figura=="g":
        dibujarG(b,car,esp)
    elif figura=="H" or figura=="h":
        dibujarH(b,car,esp)
    elif figura=="I" or figura=="i":
        dibujarI(b,car,esp)
    else:
        print("La opcion es incorrecta")
        dibujar(b,car,esp)

def main():
    b = comprobarB("Ingrese el lado del cuadrado (debe ser >= 5 e impar): ")
    car = comprobarCarYEsp("Ingrese un caracter imprimible: "," ","el caracter no puede ser un espacio, ingrese un caracter diferente: ")
    esp = comprobarCarYEsp("Ingrese un caracter imprimible distinto del anterior: ", car, "el caracter no puede ser igual al anterior, ingrese un caracter diferente: " )
    dibujar(b,car,esp)
    
main()