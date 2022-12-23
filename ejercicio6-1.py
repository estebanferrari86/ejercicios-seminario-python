def estaEnLista1(num, lista):
    return num in lista

def estaEnLista2(num, lista):
    estaEnLista = False
    for x in lista:
        if x == num:
            estaEnLista = True
    return estaEnLista

def estaEnLista3(num, lista):
    estaEnLista = False
    i = 0
    while i < len(lista) and not estaEnLista:
        if lista[i] == num:
            estaEnLista = True
        i +=1
    return estaEnLista