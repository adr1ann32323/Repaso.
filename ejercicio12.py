frutas= ["pera","mango","manzana","banana","arroz"]
print(frutas)

fruta2 = input("que fruta deseas eliminar: ")

if fruta2 in frutas:
    frutas.remove(fruta2)
    print("fruta eliminada")
    print(frutas)
else :
    print("no esta en la lista")