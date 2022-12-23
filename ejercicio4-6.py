def esCapicua(numIngresado):
    num = numIngresado
    resultado = 0
    while num != 0:
        resultado = 10*resultado+num % 10
        num//= 10
    return resultado == numIngresado

def main():
    num = int(input("Ingrese un número: "))
    if esCapicua(num):
        print(f"\nEl numero {num} es capicua")
    else:
        print(f"\nEl numero {num} no es capicua")

main()