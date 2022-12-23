def suma (a,b):
    return a+b

def resta (a,b):
    return a-b

def producto (a,b):
    return a*b

def division (a,b):
    if b !=0:
        res = a/b
    else:
        res =None
    return res

def operaciones(a,b):
    return (suma(a,b), resta(a,b), producto(a,b), division(a,b))