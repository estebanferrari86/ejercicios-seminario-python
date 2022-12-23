def agregarDicEle(dic):
    clave = int(input("ingresar número a agregar al diccionario o cero para salir: "))
    while clave != 0:
        valor = input("Ingresar el valor en letras: ")
        dic[clave] = valor
        clave = int(input("ingresar número a agregar al diccionario o cero para salir: "))
        
def mostrarValorTraducido(dic):
    clave = int(input("\ningresar número a traducir o cero para salir: "))
    while clave != 0:
        valor = dic.get(clave)
        if valor != None:
            print(clave,"->",valor)
        else:
            print("Error:", end="")
        clave = int(input("\ningresar número a traducir o cero para salir: "))

def main():
    dic = {}
    agregarDicEle(dic)
    if len(dic) > 0:
        mostrarValorTraducido(dic)
    else:
        print("el diccionario esta vacio")
        
main()