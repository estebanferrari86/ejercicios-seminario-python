def tabla(num):
    print(f"\nLa tabla del {num} es:")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

def main():
    num = int(input("Ingrese el Número: "))
    tabla(num)
    
main()