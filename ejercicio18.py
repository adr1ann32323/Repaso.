lista = [1,2,3,4,5,6,7,8]
print(lista)
num = int(input("que numero deseas agregar a la lista: "))
posicion = int(input("en que posicion (entre 0 y 7): "))

lista.insert(posicion, num)
print("lista actualizada", lista)