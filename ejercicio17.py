lista = ["adrian","alexis","diego","isabella","laura","carolina","alexis","adrian"]
print(lista)
name = (input("ingresa un nombre para contar: "))
if name in lista :
    veces = lista.count(name)
    print(f"el nombre {name} esta en la lista {veces} veces.")
else :
    print(f"el nombre {name} no esta en la lista")
