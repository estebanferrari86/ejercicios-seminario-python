def operar(num1, num2, operador):
    if operador=="+":
        res = num1 + num2
    elif operador=="-":
        res = num1 - num2
    elif operador=="*":
        res = num1 * num2
    elif operador=="/":
        res = num1 / num2
    elif operador=="//":
        res = num1 // num2
    elif operador=="**":
        res = num1 ** num2
    else:
        res = "Error!"
    return res

def ingresarOperacion():
    ope = "a"
    while ope!="+" and ope!="-" and ope!="*" and ope!="/" and ope!="//" and ope!="**" :
        ope = input("Ingrese la operación (+,-,*,/,//,**): ")
    return ope
    
def main():
    num1 = int(input("Ingrese el primer número:"))
    num2 = int(input("Ingrese el segundo número:"))
    ope = ingresarOperacion()
    res = operar(num1, num2, ope)
    print(str(num1),ope,str(num2), "=", str(res))
    
main()