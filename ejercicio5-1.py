def cambiarMayusXMinus(palabra):
    letras = { "A":"a", "B":"b", "C":"c", "D":"d", "E":"e",
             "F":"f","G":"g","H":"h","I":"i","J":"j","K":"k",
             "L":"l", "M":"m", "N":"n", "Ñ":"n", "O":"o",
             "P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u",
             "V":"v","W":"w","X":"x","Y":"y","Z":"z"
             }
    palabraSinMayusculas = ""
    for letra in palabra:
        if letra in letras:
            palabraSinMayusculas += letras[letra]
        else:
            palabraSinMayusculas += letra
    return palabraSinMayusculas
            
def borrarPuntuacion(palabra):
    simbolos = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    palabraSinPuntuacion = ""
    for letra in palabra:
        if letra not in simbolos:
            palabraSinPuntuacion += letra
    return palabraSinPuntuacion

def principioFin (texto):
    textoObj = texto.split()
    primeraSinPuntuacion = borrarPuntuacion(textoObj[0])
    ultimaSinPuntuacion = borrarPuntuacion(textoObj[-1])
    ultimaSinMayus = cambiarMayusXMinus(ultimaSinPuntuacion)
    primeraSinMayus = cambiarMayusXMinus(primeraSinPuntuacion)
    return ultimaSinMayus == primeraSinMayus

def main():
    texto = input("Ingrese un texto: ")
    if principioFin(texto):
        print("El texto cumple la condición")
    else:
        print("El texto no cumple la condición")

main()
