import random

def aleatorio(a,b):
    numero = random.randrange(a, b, 1)
    return numero

def main():
    limiteInf = int(input("Ingrese el limite inferior (numero natural): "))
    limiteSup = int(input("Ingrese el limite superirior (numero natural): "))
    numeroGenerado = aleatorio(limiteInf, limiteSup)
    numeroGenerado2 = aleatorio(numeroGenerado, limiteSup)
    numeroGenerado3 = aleatorio(numeroGenerado, numeroGenerado2)
    print(f"\nLimite inferior {limiteInf}, limite superior {limiteSup}. Numero generado: {numeroGenerado}")
    print(f"Limite inferior {numeroGenerado}, limite superior {limiteSup}. Numero generado: {numeroGenerado2}")
    print(f"Limite inferior {numeroGenerado}, limite superior {numeroGenerado2}. Numero generado: {numeroGenerado3}")

main()