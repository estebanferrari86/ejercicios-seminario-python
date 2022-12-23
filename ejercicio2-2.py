def ingresarNumeroDeTresCifras(a):
    num = 0
    while num >= 1000 or num <= 99:
        num = int(input("Ingrese el " + a + " (el numero tiene que ser de tres cifras): "))
    return num
    
def producto (a, b):
    print("\n{:10}".format(a))
    print("{}{:9}".format("x",b))
    print("----------")
    print("{:10}".format(a*(int(str(b)[2]))))
    print("{:=+9d}{}".format(a*(int(str(b)[1])) ,"-"))
    print("{:8}{}".format(a*(int(str(b)[0])) ,"--"))
    print("----------")
    print("{:10}".format(a*b))
    

def main():
    multiplicando = ingresarNumeroDeTresCifras("multiplicando")
    multiplicador = ingresarNumeroDeTresCifras("multiplicador")
    producto(multiplicando, multiplicador)
    

main()