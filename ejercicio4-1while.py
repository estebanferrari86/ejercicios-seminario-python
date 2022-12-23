def tabla(num):
    i = 1
    print(f"\nLa tabla del {num} es:")
    while i <=10:
        print(f"{num} x {i} = {num*i}")
        i +=1

def main():
    num = int(input("Ingrese el Número: "))
    tabla(num)
    
main()