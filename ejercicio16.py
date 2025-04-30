lista = [1,2,3,4,5,6,7,8,9,23]
num = int(input("ingresa un numero: "))
if num in lista:
    posicion = lista.index(num)
    print(f"el numero {num} esta en la posicion: {posicion}")
else:
    print(f"el numero {num} no esta en la lista.")