def buscarTexto(textoCorto, texto):
    largoTC = len(textoCorto)
    ultIndiceTexto = len(texto) -1
    indice = 0
    contador = 0
    if textoCorto in texto:
        while indice <= ultIndiceTexto:
            if textoCorto == texto[indice:(indice+largoTC)]:
                contador +=1
                indice += largoTC -1
            indice += 1
    return contador

def main():
    texto = input("Ingrese el texto largo: ")
    textoCorto = input("Ingrese el texto corto: ")
    vecesDeTcEnTL = buscarTexto(textoCorto, texto)
    print(f"El texto corto se encontró {vecesDeTcEnTL} veces en el texto largo")
    
main()