def agregarDicEle2(dic):
    clave = int(input("ingresar número a agregar al diccionario o cero para salir: "))
    while clave != 0:
        if clave not in list(dic.keys()):
            valorEn = input("Ingresar el valor en inglés: ")
            valorEs = input("Ingresar el valor en español: ")
            valorDe = input("Ingresar el valor en alemán: ")
            dic[clave] = (valorEs, valorEn, valorDe)
        else:
            print("Error el número ya se encuentra en el dicionario")
        clave = int(input("ingresar número a agregar al diccionario o cero para salir: "))

def cargarIdioma(idiomas):
    idioma = input("ingresar idioma ['en'|'sp'|'de'] : ")
    while idioma not in idiomas:
        idioma = input("Error, debe ingresar un idioma valido ['en'|'sp'|'de'] : ")
    return idioma

def mostrarValorTraducido(dic):
    idiomas = {"en":(1, "Inglés"), "sp":(0, "Español"), "de":(2, "Alemán")}
    clave = int(input("\ningresar número a traducir o cero para salir: "))
    while clave != 0:
        idioma = cargarIdioma(list(idiomas.keys()))
        valor = dic.get(clave)
        if valor != None:
            print(clave,"en",idiomas[idioma][1],":",valor[idiomas[idioma][0]],"\n")
        else:
            print("Error:", end="")
        clave = int(input("ingresar número a traducir o cero para salir: "))

def main():
    dic = {}
    agregarDicEle2(dic)
    if len(dic) > 0:
        mostrarValorTraducido(dic)
    else:
        print("el diccionario esta vacio")
        
main()