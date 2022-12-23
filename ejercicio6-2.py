def estaEnLista(num, lista):
    return num in lista

def cargarLista():
    res = []
    num = int(input())
    while num != 0:
        if num < 0:
            print("Error, número NO positivo.")
        elif estaEnLista(num, res):
            print("Error, número repetido.")
        else:
            res.append(num)
        num = int(input())
    return res

def main():
    print("Ingresar numeros, o 0 (cero) para terminar")
    lista = cargarLista()
    print("\nLa lista contiene:")
    print(lista)
    

main()