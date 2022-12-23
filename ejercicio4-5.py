def esPrimo(num):
    res= True
    if( num == 1 or (num%2 ==0 and num > 2)):
        res = False
    else:
        for n in range(2, int(num/2)):
            if num % n == 0:
                res = False
    return res

def imprimirHasta (num):
    print(f"\nPrimos entre 1 y {num}:")
    count = 0
    for x in range(1,num):
        if (esPrimo(x)):
            if (count > 0 and count%10 == 0) :
                print()
            print('{}{:<3}'.format("       ",x), end = "")
            count +=1

def imprimirCant (num):
    print(f"\nPrimeros {num} primos:")
    count = 0
    numerosPrimos = 0
    while numerosPrimos < num:
        if (esPrimo(count) and count > 0):
            if (numerosPrimos > 0 and numerosPrimos%10 == 0) :
                print()
            print('{}{:<3}'.format("       ",count), end = "")
            numerosPrimos +=1
        count +=1

def main():
    num= int(input("Ingrese cantidad (numero natural): "))
    imprimirHasta(num)
    imprimirCant(num)
    
main()