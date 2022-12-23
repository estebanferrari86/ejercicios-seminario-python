def sacarMayusYAcento(texto):
    letras = { "A":"a", "B":"b", "C":"c", "D":"d", "E":"e",
             "F":"f","G":"g","H":"h","I":"i","J":"j","K":"k",
             "L":"l", "M":"m", "N":"n", "Ñ":"n","O":"o",
             "P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u",
             "V":"v","W":"w","X":"x","Y":"y","Z":"z","á":"a",
             "é":"e","í":"i","ó":"o","ú":"u","Á":"a","É":"e",
             "Í":"i","Ó":"o","Ú":"u"
             }
    textoFinal = ""
    for letra in texto:
        if letra in letras:
            textoFinal += letras[letra]
        else:
            textoFinal += letra
    return textoFinal


def borrarPuntuacion(texto):
    simbolos = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    textoSinPuntuacion = ""
    for letra in texto:
        if letra not in simbolos:
            textoSinPuntuacion += letra
    return textoSinPuntuacion

def esPalindromo(texto):
    textoInvertido = ""
    num = len(texto) -1
    while num >= 0:
        textoInvertido += texto[num]
        num -= 1
    return texto == textoInvertido
        
def main():
    texto = input("Ingrese una frase: ")
    textoLimpio = sacarMayusYAcento(borrarPuntuacion(texto))
    if esPalindromo(textoLimpio):
        print("La frase es palíndroma")
    else:
        print("La frase no es palíndroma")

main()        
        
        
        
        