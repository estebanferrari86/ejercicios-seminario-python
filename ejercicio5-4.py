def palabraMasLarga(texto):
    textoObj = texto.split()
    palabraMasLarga = textoObj[0]
    for palabra in textoObj:
        if len(palabra) > len(palabraMasLarga):
            palabraMasLarga = palabra
    return palabraMasLarga

def palabraMasCorta(texto):
    textoObj = texto.split()
    palabraMasCorta = textoObj[0]
    for palabra in textoObj:
        if len(palabra) < len(palabraMasCorta):
            palabraMasCorta = palabra
    return palabraMasCorta

def cantPalabras(texto):
    textoObj = texto.split
    return len(textoObj)

def borrarPuntuacion(palabra):
    simbolos = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    palabraSinPuntuacion = ""
    for letra in palabra:
        if letra not in simbolos:
            palabraSinPuntuacion += letra
    return palabraSinPuntuacion


def main():
    texto = input("Ingrese un texto: ")
    textoSinPun = borrarPuntuacion(texto)
    cantDePalabras = cantPalabras(textoSinPun)
    palabraCorta = palabraMasCorta(textoSinPun)
    palabraLarga = palabraMasLarga(textoSinPun)
    print(f'\nEl texto tiene {cantDePalabras} palabras, la de mayor longitud es "{palabraLarga}" y la de menor longitud es "{palabraCorta}".')
    
    
main()
